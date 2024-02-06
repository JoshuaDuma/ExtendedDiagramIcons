import os
import sys
from typing import Iterable
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template, exceptions

import config as cfg
from . import app_root_dir, doc_root_dir, resource_dir, template_dir, base_dir

_usage = "Usage: generate.py <provider>"

def make_directories(path):
    # Ensure the directory exists
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return True

def load_tmpl(tmpl: str) -> Template:
    env = Environment(loader=FileSystemLoader(template_dir()))
    env.filters["up_or_title"] = up_or_title
    return env.get_template(tmpl)


def up_or_title(pvd: str, s: str) -> str:
    if s in cfg.UPPER_WORDS.get(pvd, ()):
        return s.upper()
    if s in cfg.TITLE_WORDS.get(pvd, {}):
        return cfg.TITLE_WORDS[pvd][s]
    return s.title()

def relative_directory_depth_with_parent(relative_path):
    """
    Returns the depth of a directory structure relative to the current working directory.
    The string representation of the directory level uses ".parent" for each level.
    For example, if the relative_path is 'a/b/c', and all exist, the depth is 3 and the
    string will be '.parent.parent.parent'.

     Example usage:
    # Please run this on your local machine with a valid relative directory path as this environment
    # does not have access to an actual filesystem.

    # relative_path = 'a/b/c'  # Replace with the relative path you want to check
    # depth, parent_string = relative_directory_depth_with_parent(relative_path)
    # print(f"Depth: {depth}, Parent String: {parent_string}")
    """
    depth = 0
    parent_str = ""
    current_path = os.path.abspath(relative_path)
    
    while os.path.dirname(current_path) != current_path:  # Check if we've reached the root
        # Adjust for current directory
        if os.path.exists(current_path) and depth > 3:
            parent_str = '.parent' + parent_str
        current_path = os.path.dirname(current_path)
        depth += 1
        
    return parent_str


def gen_classes(pvd: str, typ: str, paths: Iterable[str]) -> str:
    """Generate all service node classes based on resources paths with class templates."""
    tmpl = load_tmpl(cfg.TMPL_MODULE)

    # TODO: extract the gen class metas for sharing
    # TODO: independent function for generating all pvd/typ/paths pairs
    def _gen_class_meta(path: str) -> dict:
        base = os.path.splitext(path)[0]
        name = "".join([up_or_title(pvd, s) for s in base.split("-")])
        return {"name": name, "icon": path}

    mod_path = os.path.join(app_root_dir(pvd), f"{typ}.py")
    # To get the relative path with respect to the application root directory:
    common_path = Path(__file__).parent  # This would be your common path
    relative_path = os.path.relpath(mod_path, common_path)
    dir_lvl = relative_directory_depth_with_parent(relative_path)
    metas = map(_gen_class_meta, paths)
    aliases = cfg.ALIASES[pvd][typ] if typ in cfg.ALIASES[pvd] else {}
    return tmpl.render(dir_lvl=dir_lvl, pvd=pvd, typ=typ, metas=metas, aliases=aliases)


def gen_apidoc(pvd: str, typ_paths: dict) -> str:
    try:
      default_tmp = cfg.TMPL_APIDOC.split('.')
      tmpl_file = f"{default_tmp[0]}_{pvd}.{default_tmp[1]}"
      tmpl = load_tmpl(tmpl_file)
    except exceptions.TemplateNotFound:
      tmpl = load_tmpl(cfg.TMPL_APIDOC)

    # TODO: remove
    def _gen_class_name(path: str) -> str:
        base = os.path.splitext(path)[0]
        name = "".join([up_or_title(pvd, s) for s in base.split("-")])
        return name

    typ_classes = {}
    for typ, (paths, resource_root) in sorted(typ_paths.items()):
        typ_classes[typ] = []
        for path in paths:
            name = _gen_class_name(path)
            resource_path = os.path.join(resource_root, path)
            alias = cfg.ALIASES[pvd].get(typ, {}).get(name)
            app_root = cfg.DIR_APP_ROOT
            typ_classes[typ].append({"name": name, "alias": alias, "resource_path": resource_path, "app_root": app_root})
    return tmpl.render(pvd=pvd, typ_classes=typ_classes)


def make_module(pvd: str, typ: str, classes: str) -> None:
    """Create a module file"""
    mod_path = os.path.join(app_root_dir(pvd), f"{typ}.py")
    make_directories(mod_path)
    with open(mod_path, "w+") as f:
        f.write(classes)


def make_apidoc(pvd: str, content: str) -> None:
    """Create an api documentation file"""
    mod_path = os.path.join(doc_root_dir(), f"{pvd}.md")
    make_directories(mod_path)
    with open(mod_path, "w+") as f:
        f.write(content)


def generate(pvd: str) -> None:
    """Generates a service node classes."""
    typ_paths = {}
    base = base_dir()
    for root, _, files in os.walk(resource_dir(pvd)):
        # Extract the names and paths from resources.
        files.sort()
        pngs = list(filter(lambda f: f.endswith(".png"), files))
        paths = list(filter(lambda f: "rounded" not in f, pngs))

        # Skip the top-root directory.
        typ = os.path.basename(root)
        
        if typ == pvd:
            continue

        resource_root = os.path.relpath(root, base)
        classes = gen_classes(pvd, typ, paths)
        make_module(pvd, typ, classes)

        typ_paths[typ] = (paths, resource_root)
    # Build API documentation
    apidoc = gen_apidoc(pvd, typ_paths)
    make_apidoc(pvd, apidoc)


if __name__ == "__main__":
    pvd = sys.argv[1]
    if pvd not in cfg.PROVIDERS:
        sys.exit()
    generate(pvd)