import os

def concatenate_md_files_to_string(source_dir):
    """
    Concatenate all .md files from the source directory into a single string.

    :param source_dir: Directory containing .md files.
    :return: A string with the concatenated content of all .md files.
    """
    content = ""
    for filename in os.listdir(source_dir):
        if filename.endswith('.md'):
            file_path = os.path.join(source_dir, filename)
            with open(file_path, 'r') as md_file:
                content += md_file.read() + '\n\n'
    return content

def update_readme_section(readme_path, new_content, start_marker, end_marker):
    with open(readme_path, 'r') as file:
        readme_content = file.readlines()
    
    start_index = next(i for i, line in enumerate(readme_content) if start_marker in line)
    end_index = next(i for i, line in enumerate(readme_content) if end_marker in line)

    updated_content = readme_content[:start_index + 1] + [new_content + '\n'] + readme_content[end_index:]
    
    with open(readme_path, 'w') as file:
        file.writelines(updated_content)

# Example usage
source_directory = 'docs/nodes'  # Replace with your actual directory path
concatenated_content = concatenate_md_files_to_string(source_directory)

# Now, use the existing function to update the README section
readme_path = 'README.md'
start_marker = '<!-- START_SECTION:Documentation -->'
end_marker = '<!-- END_SECTION:Documentation -->'
update_readme_section(readme_path, concatenated_content, start_marker, end_marker)