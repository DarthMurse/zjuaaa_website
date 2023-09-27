import json
import os
from PIL import Image

img_info_template = {
    'image-name': '',
    'full-image': '',
    'thumbnail-image': '',
    'middle-image': '',
    'histogram-image': '',
    'skyplot-image': '',
    'base-information': {
        'photographer': '',
        'target-name': '',
        'sky-plot': '',
        'upload-date': '',
        'image-description': ''
    },
    'shoot-information': {
        'shoot-date': '',
        'location': '',
        'exposure': ''
    },
    'equipment': {
        'telescope': '',
        'camera': '',
        'mount': '',
        'filter': '',
        'guide-camera': '',
        'focuser': '',
        'accessory': '',
        'software': ''
    },
    'advanced': {
        'file-size': '',
        'resolution': '',
        'RA': '',
        'DEC': '',
        'pixel-scale': '',
        'FOV': ''
    }
}


class img_info:

    def __init__(self, filename, info_in=None):
        self.filename = filename
        self.info = img_info_template.copy()
        if info_in:
            for key in info_in:
                if key in self.info:
                    if isinstance(self.info[key], dict):
                        for sub_key in info_in[key]:
                            if sub_key in self.info[key]:
                                self.info[key][sub_key] = info_in[key][sub_key]
                    else:
                        self.info[key] = info_in[key]

    def get_all_info(self):
        return self.info

    def get_key_info(self, key_name):
        if key_name in self.info:
            return self.info[key_name]
        else:
            return None

    def set_key_info(self, key_name, key_info):
        finished = 0
        for key in self.info:
            if key == key_name:
                self.info[key] = key_info
                finished = 1
                break
            if isinstance(self.info[key], dict):
                for sub_key in self.info[key]:
                    if sub_key == key_name:
                        self.info[key][sub_key] = key_info
                        finished = 1
                        break
                if finished:
                    break
        return finished

    def set_base_info(self, base_info):
        for key in base_info:
            if key in self.info['base-information']:
                self.info['base-information'][key] = base_info[key]

    def set_shoot_info(self, shoot_info):
        for key in shoot_info:
            if key in self.info['shoot-information']:
                self.info['shoot-information'][key] = shoot_info[key]

    def set_equipment_info(self, equipment_info):
        for key in equipment_info:
            if key in self.info['equipment']:
                self.info['equipment'][key] = equipment_info[key]

    def set_advanced_info(self, advanced_info):
        for key in advanced_info:
            if key in self.info['advanced']:
                self.info['advanced'][key] = advanced_info[key]

    def get_base_info(self):
        return self.info['base-information']

    def get_shoot_info(self):
        return self.info['shoot-information']

    def get_equipment_info(self):
        return self.info['equipment']

    def get_advanced_info(self):
        return self.info['advanced']


image_name = input("请输入图片名称：")
image_file_name = input("请输入图片文件名：")
full_image = "/masterpiece/full/" + "full_" + image_file_name + ".png"
thumbnail_image = "/masterpiece/thumbnail/" + "thumbnail_" + image_file_name + ".png"
middle_image = "/masterpiece/middle/" + "middle_" + image_file_name + ".png"
histogram_image = "/masterpiece/histogram/" + "histogram_" + image_file_name + ".png"
print("没有的信息可留空或填无，留空则不会显示在网页上")
skyplot_image = input("请输入天区图路径：")
photographer = input("请输入拍摄/后期的作者（甲/乙，为同一人则输入一个名字即可）：")
target_name = input("请输入目标名称：")
sky_plot = input("请输入图片所属天区：")
# update_date = input("请输入上传日期（yyyy/m/d）：")
image_description = input("请输入图片描述：")
shoot_date = input("请输入拍摄日期（yyyy/m/d，多个日期用空格分隔）")
location = input("请输入拍摄地点：")
exposure = input("请输入曝光时间，分通道：")
telescope = input("请输入望远镜：")
camera = input("请输入相机：")
mount = input("请输入底座：")
filter = input("请输入滤镜：")
guide_camera = input("请输入导星相机：")
focuser = input("请输入电动调焦：")
accessory = input("请输入附件，如有多个，请用、分隔：")
software = input("请输入软件，如有多个，请用、分隔：")
# file_size = input("请输入文件大小：")
# resolution = input("请输入分辨率：")
RA = input("请输入赤经（h m s，无需单位）：")
DEC = input("请输入赤纬（d m s，无需单位）：")
pixel_scale = input("请输入像素分辨率（x d/m/s）：")
FOV = input("请输入视场（width height d/m/s）：")

current_img_info = img_info_template.copy()
current_img_info['image-name'] = image_name
current_img_info['full-image'] = full_image
current_img_info['middle-image'] = middle_image
current_img_info['thumbnail-image'] = thumbnail_image
current_img_info['histogram-image'] = histogram_image
current_img_info['skyplot-image'] = skyplot_image
current_img_info['base-information']['photographer'] = photographer
current_img_info['base-information']['target-name'] = target_name
current_img_info['base-information']['sky-plot'] = sky_plot
current_img_info['base-information']['update-date'] = update_date
current_img_info['base-information']['image-description'] = image_description
current_img_info['shoot-information']['shoot-date'] = shoot_date
current_img_info['shoot-information']['location'] = location
current_img_info['shoot-information']['exposure'] = exposure
current_img_info['equipment']['telescope'] = telescope
current_img_info['equipment']['camera'] = camera
current_img_info['equipment']['mount'] = mount
current_img_info['equipment']['filter'] = filter
current_img_info['equipment']['guide-camera'] = guide_camera
current_img_info['equipment']['focuser'] = focuser
current_img_info['equipment']['accessory'] = accessory
current_img_info['equipment']['software'] = software
# current_img_info['advanced']['file-size'] = file_size
# current_img_info['advanced']['resolution'] = resolution
current_img_info['advanced']['RA'] = RA
current_img_info['advanced']['DEC'] = DEC
current_img_info['advanced']['pixel-scale'] = pixel_scale
current_img_info['advanced']['FOV'] = FOV





current_img_info['advanced']['file-size'] = get_file_size(os.getcwd() +
                                                          full_image)

with Image.open(os.getcwd() + full_image) as img:
    width, height = img.size
current_img_info['advanced']['resolution'] = str(width) + "x" + str(height)

print(current_img_info)

# with open("masterpiece/image_information.json", 'r', encoding='utf-8') as f:
#     data = json.loads(f.read())

# data[image_file_name] = current_img_info

# with open("masterpiece/image_information.json", 'w', encoding='utf-8') as f:
#     json.dump(data, f, indent=4, ensure_ascii=False)
