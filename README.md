# BingImageCreator
Tool query ảnh từ Bing Dall-e

## Cài đặt môi trường
  - Python >= 3.8
  - [__Visual Studio Code__](https://code.visualstudio.com/) (để lập trình) 
    hoặc 
    __Terminal(Command Prompt hoặc PowerShel)__ (để sử dụng)

## Tải bộ code 
  - Tải qua [link sau]("")

## Cài thư viện
> Đối với Terminal
  - Bấm tổ hợp __Window__ + __R__
  - Gõ __cmd__ hoặc __wt__
  - Tải thư viện qua lệnh 

`pip install -r requirement.txt`

> Đối với Visual Studio Code: 
  - Open Folder 
  - Bấm tổ hợp phím __Ctrl__ + __`__ để mở terminal
  - Paste lệnh vào terminal
`pip install --upgrade `


[Developer Documentation](https://github.com/acheong08/BingImageCreator/blob/main/DOCUMENTATION.md)


## Getting authentication
### Chromium based browsers (Edge, Opera, Vivaldi, Brave)
- Go to https://bing.com/.
- F12 to open console
- In the JavaScript console, type `cookieStore.get("_U").then(result => console.log(result.value))` and press enter
- Copy the output. This is used in `--U` or `auth_cookie`.

### Firefox
- Go to https://bing.com/.
- F12 to open developer tools
- navigate to the storage tab
- expand the cookies tab
- click on the `https://bing.com` cookie
- copy the value from the `_U`
