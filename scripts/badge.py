import sys

def update_readme_section(readme_path, new_content, start_marker, end_marker):
    with open(readme_path, 'r') as file:
        readme_content = file.readlines()
    
    start_index = next(i for i, line in enumerate(readme_content) if start_marker in line)
    end_index = next(i for i, line in enumerate(readme_content) if end_marker in line)

    updated_content = readme_content[:start_index + 1] + [new_content + '\n'] + readme_content[end_index:]
    
    with open(readme_path, 'w') as file:
        file.writelines(updated_content)

# Function to create an SVG badge with "Dev Build" on one side and a number on the other
def create_svg_badge_dev(build_number):
    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
    <g xmlns="http://www.w3.org/2000/svg" font-family="'DejaVu Sans',Verdana,Geneva,sans-serif" font-size="11">
      <path id="workflow-bg" d="M0,3 C0,1.3431 1.3552,0 3.02702703,0 L106,0 L106,20 L3.02702703,20 C1.3552,20 0,18.6569 0,17 L0,3 Z" fill="rgb(16, 16, 15)" fill-rule="nonzero"/>
      <text fill="#010101" fill-opacity=".3">
        <tspan x="22.1981982" y="15" aria-hidden="true">Dev Build</tspan>
      </text>
      <text fill="#FFFFFF">
        <tspan x="22.1981982" y="14">Dev Build</tspan>
      </text>
    </g>
    <rect x="55%" width="40%" height="100%" fill="rgb(99, 194, 97)"/>

    <text x="75%" y="70%" font-family="DejaVu Sans',Verdana,Geneva,sans-serif" font-size="11" fill="#fff" text-anchor="middle">{build_number}</text>
    <path xmlns="http://www.w3.org/2000/svg" fill="#959DA5" d="M11 3c-3.868 0-7 3.132-7 7a6.996 6.996 0 0 0 4.786 6.641c.35.062.482-.148.482-.332 0-.166-.01-.718-.01-1.304-1.758.324-2.213-.429-2.353-.822-.079-.202-.42-.823-.717-.99-.245-.13-.595-.454-.01-.463.552-.009.946.508 1.077.718.63 1.058 1.636.76 2.039.577.061-.455.245-.761.446-.936-1.557-.175-3.185-.779-3.185-3.456 0-.762.271-1.392.718-1.882-.07-.175-.315-.892.07-1.855 0 0 .586-.183 1.925.718a6.5 6.5 0 0 1 1.75-.236 6.5 6.5 0 0 1 1.75.236c1.338-.91 1.925-.718 1.925-.718.385.963.14 1.68.07 1.855.446.49.717 1.112.717 1.882 0 2.686-1.636 3.28-3.194 3.456.254.219.473.639.473 1.295 0 .936-.009 1.689-.009 1.925 0 .184.131.402.481.332A7.011 7.011 0 0 0 18 10c0-3.867-3.133-7-7-7z"/>
</svg>"""
    return svg_template

# Function to create an SVG badge with "Stable Build" on one side and a number on the other
def create_svg_badge_stable(build_number):
    svg_template = f"""<svg xmlns="http://www.w3.org/2000/svg" width="150" height="20">
    <g xmlns="http://www.w3.org/2000/svg" font-family="'DejaVu Sans',Verdana,Geneva,sans-serif" font-size="11">
      <path id="workflow-bg" d="M0,3 C0,1.3431 1.3552,0 3.02702703,0 L106,0 L106,20 L3.02702703,20 C1.3552,20 0,18.6569 0,17 L0,3 Z" fill="rgb(16, 16, 15)" fill-rule="nonzero"/>
      <text fill="#010101" fill-opacity=".3">
        <tspan x="22.1981982" y="15" aria-hidden="true">Stable Build</tspan>
      </text>
      <text fill="#FFFFFF">
        <tspan x="22.1981982" y="14">Stable Build</tspan>
      </text>
    </g>
    <g xmlns="http://www.w3.org/2000/svg" transform="translate(106)" font-family="'DejaVu Sans',Verdana,Geneva,sans-serif" font-size="11">
      <path d="M0 0h46.939C48.629 0 50 1.343 50 3v14c0 1.657-1.37 3-3.061 3H0V0z" id="state-bg" fill="rgb(99, 194, 97)" fill-rule="nonzero"/>
      <text fill="#010101" fill-opacity=".3" aria-hidden="true">
        <tspan x="4" y="15">{build_number}</tspan>
      </text>
      <text fill="#FFFFFF">
        <tspan x="4" y="14">{build_number}</tspan>
      </text>
    </g>
    <path xmlns="http://www.w3.org/2000/svg" fill="#959DA5" d="M11 3c-3.868 0-7 3.132-7 7a6.996 6.996 0 0 0 4.786 6.641c.35.062.482-.148.482-.332 0-.166-.01-.718-.01-1.304-1.758.324-2.213-.429-2.353-.822-.079-.202-.42-.823-.717-.99-.245-.13-.595-.454-.01-.463.552-.009.946.508 1.077.718.63 1.058 1.636.76 2.039.577.061-.455.245-.761.446-.936-1.557-.175-3.185-.779-3.185-3.456 0-.762.271-1.392.718-1.882-.07-.175-.315-.892.07-1.855 0 0 .586-.183 1.925.718a6.5 6.5 0 0 1 1.75-.236 6.5 6.5 0 0 1 1.75.236c1.338-.91 1.925-.718 1.925-.718.385.963.14 1.68.07 1.855.446.49.717 1.112.717 1.882 0 2.686-1.636 3.28-3.194 3.456.254.219.473.639.473 1.295 0 .936-.009 1.689-.009 1.925 0 .184.131.402.481.332A7.011 7.011 0 0 0 18 10c0-3.867-3.133-7-7-7z"/>
</svg>"""
    return svg_template

type = sys.argv[1] if len(sys.argv) > 1 else "unknown"

if type == "stable":
    # Taking argument from bash (the build number) and storing it in a variable
    build_number = sys.argv[2] if len(sys.argv) > 1 else "unknown"

    # Create the SVG badge
    svg_badge = create_svg_badge_stable(build_number)

    # Save the SVG badge to a file
    with open("docs/data/stable_build.svg", "w") as file:
        file.write(svg_badge)

    print("SVG badge created with build number:", build_number)

    string = f"""
- Install latest stable build: `pip install ExtendedDiagramIcons=={build_number}`
    """

    # Now, use the existing function to update the README section
    readme_path = 'README.md'
    start_marker = '<!-- START_SECTION:InstallLatestStable -->'
    end_marker = '<!-- END_SECTION:InstallLatestStable -->'
    update_readme_section(readme_path, string, start_marker, end_marker)
    
    readme_path = 'README.md'
    start_marker = '<!-- START_SECTION:InstallLatestDevelopment -->'
    end_marker = '<!-- END_SECTION:InstallLatestDevelopment -->'
    update_readme_section(readme_path, "", start_marker, end_marker)

    print("Updated README.mdwith build number:", build_number)

elif type == "dev":
    # Taking argument from bash (the build number) and storing it in a variable
    build_number = sys.argv[2] if len(sys.argv) > 1 else "unknown"

    # Create the SVG badge
    svg_badge = create_svg_badge_dev(build_number)

    # Save the SVG badge to a file
    with open("docs/data/development_build.svg", "w") as file:
        file.write(svg_badge)

    print("SVG badge created with build number:", build_number)

    string = f"""
- Install latest development build: `pip install ExtendedDiagramIcons=={build_number}`
    """

    # Now, use the existing function to update the README section
    readme_path = 'README.md'
    start_marker = '<!-- START_SECTION:InstallLatestDevelopment -->'
    end_marker = '<!-- END_SECTION:InstallLatestDevelopment -->'
    update_readme_section(readme_path, string, start_marker, end_marker)

    start_marker = '<!-- START_SECTION:InstallLatestStable -->'
    end_marker = '<!-- END_SECTION:InstallLatestStable -->'
    update_readme_section(readme_path, "", start_marker, end_marker)

    print("Updated README.mdwith build number:", build_number)

