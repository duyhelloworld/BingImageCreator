from BingImageCreator import ImageGen

def excute(prompt="Cat"):
    print("test function")
    cookie = '1iAc-_ASX1Rb_402WIK_ihn9B0W6CgpSZooU8v4XzS1jrt8nEQNiNP9n2uNmIrUFEtoOWv3NZnsggczOB7xW7HalAHHwCd_Cb4koj0imKWgaxbwN_XqhAU6-sNxN6Ne6GnD87scuXMt44hsFf6o3sGGYpEu4OD9q3PK_uYS-BW2OpMDYWPyclXkN4PslMXdS2Mgo3THahB3H2nqSxu4sNgg'
    gen = ImageGen(auth_cookie=cookie)
    image_urls = gen.get_images(prompt)
    gen.save_images(
        links=image_urls, output_dir="src/images", file_name=prompt.lower().split(" ")[0], download_count=4)
excute("Ironman 3D, visualize, ultralistic")