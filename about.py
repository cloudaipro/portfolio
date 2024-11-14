import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY'

def generate_image(prompt, n=1, size="1024x1024"):
    """
    Function to generate an image based on the provided prompt.

    Args:
    - prompt (str): The text description for the image to be generated.
    - n (int): Number of images to generate.
    - size (str): Size of the generated image, default is 1024x1024.

    Returns:
    - image_urls (list): List of URLs of generated images.
    """
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size
        )
        image_urls = [data['url'] for data in response['data']]
        return image_urls
    
    except Exception as e:
        print(f"Error generating image: {e}")
        return None

# Example prompt based on your previous description
prompt_text = "A minimalist illustration featuring a senior software engineer working in a bright, organized workspace. The focus is on the engineer at their desk, intently working on a laptop displaying lines of code and project flowcharts, highlighting their expertise in software development."

# Generate image
image_urls = generate_image(prompt_text)
if image_urls:
    for idx, url in enumerate(image_urls):
        print(f"Image {idx+1} URL: {url}")
