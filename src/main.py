from BingImageCreator import ImageGen

# Cookie vứt vào trong dấu ' ở dưới đây
COOKIE = 'bla bla...'

# PROMPT vứt vào đây
PROMPT = 'Mèo Doraemon'

def excute(prompt):
    print("_______________________________________")
    print("__________Bing AI Image Creator________")
    print("_______________________________________\n")
    gen = ImageGen(auth_cookie=COOKIE)
    image_urls = gen.get_images(prompt)
    gen.save_images(
        links=image_urls, output_dir="src/images",
        file_name=prompt.lower().split(" ")[0], download_count=4)
    
excute(PROMPT)