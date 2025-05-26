import os
import urllib.parse

def generate_markdown_links(directory='products/best/1'):
    """Generate markdown links for all .md files in the directory"""
    links = []
    
    # Get all .md files in the directory
    for filename in sorted(os.listdir(directory)):
        if filename.endswith('.md'):
            # Remove .md extension for display text
            display_text = filename[:-3]
            
            # URL encode the filename for the link
            encoded_filename = urllib.parse.quote(filename)
            
            # Create the GitHub URL
            url = f"https://github.com/boxingundefeated/content/blob/main/{directory}/{encoded_filename}"
            
            # Create markdown link
            markdown_link = f"- [{display_text}]({url})"
            links.append(markdown_link)
    
    return links

def save_links_to_file(links, output_file='sitemap_links.md'):
    """Save the generated links to a file"""
    with open(output_file, 'w') as f:
        f.write('\n'.join(links))
    print(f"Links saved to {output_file}")

def append_to_readme(links):
    """Append links to README.md"""
    with open('README.md', 'a') as f:
        f.write('\n'.join(links))
    print("Links appended to README.md")

if __name__ == "__main__":
    # Generate all links
    links = generate_markdown_links()
    
    # Print first 10 links as preview
    print("Preview of first 10 links:")
    for link in links[:10]:
        print(link)
    
    print(f"\nTotal links generated: {len(links)}")
    
    # Save to a separate file
    save_links_to_file(links)
    
    # Or append to README (uncomment if needed)
    # append_to_readme(links)