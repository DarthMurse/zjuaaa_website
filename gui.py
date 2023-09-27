import tkinter as tk
from tkinter import ttk
from tkinter import N, S, W, E
from tkinter import messagebox, filedialog
from tkcalendar import Calendar

from PIL import Image, ImageTk

from typing import List, Dict

import copy
import os
import json
import re

img_info_template = {
    'file-name': '',
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


class img_info_class:

    def __init__(self, index: int = None, info_in: dict = None):
        self.index = index
        self.info = copy.deepcopy(img_info_template)
        if info_in:
            for key in info_in:
                if key in self.info:
                    if isinstance(self.info[key], dict):
                        for sub_key in info_in[key]:
                            if sub_key in self.info[key]:
                                self.info[key][sub_key] = info_in[key][sub_key]
                    else:
                        self.info[key] = info_in[key]

    def clear(self):
        self.index = None
        self.info = copy.deepcopy(img_info_template)

    def strip_all_value(self):
        for key in self.info:
            if isinstance(self.info[key], dict):
                for sub_key in self.info[key]:
                    self.info[key][sub_key] = self.info[key][sub_key].strip()
            else:
                self.info[key] = self.info[key].strip()

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

    def set_file_name(self, file_name):
        self.info['file-name'] = file_name

    def set_img_name(self, name):
        self.info['image-name'] = name

    def set_img_path(self, file_name):
        base_path = '/masterpiece/'
        self.info['full-image'] = base_path + 'full/full_' + file_name
        self.info[
            'thumbnail-image'] = base_path + 'thumbnail/thumbnail_' + os.path.splitext(
                file_name)[0] + '.png'
        self.info[
            'middle-image'] = base_path + 'middle/middle_' + os.path.splitext(
                file_name)[0] + '.png'
        self.info[
            'histogram-image'] = base_path + 'histogram/histogram_' + os.path.splitext(
                file_name)[0] + '.png'

    def set_skyplot_path(self, path):
        self.info['skyplot-image'] = path

    def set_photographer(self, photographer):
        self.info['base-information']['photographer'] = photographer

    def set_target_name(self, target_name):
        self.info['base-information']['target-name'] = target_name

    def set_skyplot(self, sky_plot):
        self.info['base-information']['sky-plot'] = sky_plot

    def set_upload_date(self, upload_date):
        self.info['base-information']['upload-date'] = upload_date

    def set_image_description(self, image_description):
        self.info['base-information']['image-description'] = image_description

    def set_shoot_date(self, shoot_date):
        self.info['shoot-information']['shoot-date'] = shoot_date

    def set_location(self, location):
        self.info['shoot-information']['location'] = location

    def set_exposure(self, exposure):
        self.info['shoot-information']['exposure'] = exposure

    def set_telescope(self, telescope):
        self.info['equipment']['telescope'] = telescope

    def set_camera(self, camera):
        self.info['equipment']['camera'] = camera

    def set_mount(self, mount):
        self.info['equipment']['mount'] = mount

    def set_filter(self, filter):
        self.info['equipment']['filter'] = filter

    def set_guide_camera(self, guide_camera):
        self.info['equipment']['guide-camera'] = guide_camera

    def set_focuser(self, focuser):
        self.info['equipment']['focuser'] = focuser

    def set_accessory(self, accessory):
        self.info['equipment']['accessory'] = accessory

    def set_software(self, software):
        self.info['equipment']['software'] = software

    def set_file_size(self, file_size):
        self.info['advanced']['file-size'] = file_size

    def set_resolution(self, resolution):
        self.info['advanced']['resolution'] = resolution

    def set_RA(self, h, m, s):
        if h == '' or m == '' or s == '':
            self.info['advanced']['RA'] = ''
        else:
            self.info['advanced']['RA'] = h + 'h' + m + 'm' + s + 's'

    def set_DEC(self, d, m, s):
        if d == '' or m == '' or s == '':
            self.info['advanced']['DEC'] = ''
        else:
            self.info['advanced']['DEC'] = d + '°' + m + '\'' + s + '"'

    def set_pixel_scale(self, pixel_scale, unit):
        if pixel_scale == '':
            self.info['advanced']['pixel-scale'] = ''
        else:
            self.info['advanced']['pixel-scale'] = pixel_scale + ' ' + unit

    def set_FOV(self, width, height, unit):
        if width == '' or height == '':
            self.info['advanced']['FOV'] = ''
        else:
            self.info['advanced']['FOV'] = width + ' x ' + height + ' ' + unit

    def get_file_name(self):
        return self.info['file-name']

    def get_img_name(self):
        return self.info['image-name']

    def get_img_path(self):
        return self.info['full-image']

    def get_skyplot_path(self):
        return self.info['skyplot-image']

    def get_thumbnail_path(self):
        return self.info['thumbnail-image']

    def get_middle_path(self):
        return self.info['middle-image']

    def get_histogram_path(self):
        return self.info['histogram-image']

    def get_photographer(self):
        return self.info['base-information']['photographer']

    def get_target_name(self):
        return self.info['base-information']['target-name']

    def get_skyplot(self):
        return self.info['base-information']['sky-plot']

    def get_upload_date(self):
        return self.info['base-information']['upload-date']

    def get_image_description(self):
        return self.info['base-information']['image-description']

    def get_shoot_date(self):
        return self.info['shoot-information']['shoot-date']

    def get_location(self):
        return self.info['shoot-information']['location']

    def get_exposure(self):
        return self.info['shoot-information']['exposure']

    def get_telescope(self):
        return self.info['equipment']['telescope']

    def get_camera(self):
        return self.info['equipment']['camera']

    def get_mount(self):
        return self.info['equipment']['mount']

    def get_filter(self):
        return self.info['equipment']['filter']

    def get_guide_camera(self):
        return self.info['equipment']['guide-camera']

    def get_focuser(self):
        return self.info['equipment']['focuser']

    def get_accessory(self):
        return self.info['equipment']['accessory']

    def get_software(self):
        return self.info['equipment']['software']

    def get_file_size(self):
        return self.info['advanced']['file-size']

    def get_resolution(self):
        return self.info['advanced']['resolution']

    def get_RA(self, hms):
        if self.info['advanced']['RA'] == '':
            return ''

        match hms:
            case 'h':
                return self.info['advanced']['RA'].split('h')[0]
            case 'm':
                return self.info['advanced']['RA'].split('h')[1].split('m')[0]
            case 's':
                return self.info['advanced']['RA'].split('h')[1].split(
                    'm')[1].split('s')[0]

    def get_DEC(self, dms):
        if self.info['advanced']['DEC'] == '':
            return ''

        match dms:
            case 'd':
                return self.info['advanced']['DEC'].split('°')[0]
            case 'm':
                return self.info['advanced']['DEC'].split('°')[1].split('"')[0]
            case 's':
                return self.info['advanced']['DEC'].split('°')[1].split(
                    '\'')[1].split('"')[0]

    def get_pixel_scale(self):
        if self.info['advanced']['pixel-scale'] == '':
            return '', '"/px'

        unit = self.info['advanced']['pixel-scale'][-4:]
        number = self.info['advanced']['pixel-scale'][:-5]
        return number, unit

    def get_FOV(self):
        if self.info['advanced']['FOV'] == '':
            return '', '', '"'

        unit = self.info['advanced']['FOV'][-1:]
        width = self.info['advanced']['FOV'][:-2].split(' x ')[0]
        hide = self.info['advanced']['FOV'][:-2].split(' x ')[1]
        return width, hide, unit

    def get_base_info(self):
        return self.info['base-information']

    def get_shoot_info(self):
        return self.info['shoot-information']

    def get_equipment_info(self):
        return self.info['equipment']

    def get_advanced_info(self):
        return self.info['advanced']


class img_list_json_class:

    def __init__(self, img_info_list: List[img_info_class] = []):
        self.img_info_list = img_info_list

    def load_json(self, json_path):
        with open(json_path, 'r', encoding='utf-8') as f:
            for key, value in json.load(f).items():
                self.img_info_list.append(img_info_class(key, value))

    def save_json(self, json_path):
        with open(json_path, 'w') as f:

            save_dict = {}
            for item in self.img_info_list:
                save_dict[item.index] = item.get_all_info()
            json.dump(save_dict, f, indent=4, ensure_ascii=False)

    def add_img(self, img_info: img_info_class):
        img_info.strip_all_value()
        self.img_info_list.append(img_info)

    def delete_img(self, index):
        self.img_info_list.pop(int(index) - 1)
        for i in range(int(index) - 1, len(self.img_info_list)):
            self.img_info_list[i].index = i + 1

    def edit_img(self, index, img_info: img_info_class):
        img_info.strip_all_value()
        self.img_info_list[int(index) - 1] = img_info

    def get_img(self, index):
        return self.img_info_list[int(index) - 1]

    def swap_img(self, index1, index2):
        self.img_info_list[index1 - 1], self.img_info_list[
            index2 - 1] = self.img_info_list[index2 -
                                             1], self.img_info_list[index1 - 1]
        self.img_info_list[index1 - 1].set_img_index(index1 - 1)
        self.img_info_list[index2 - 1].set_img_index(index2 - 1)

    def get_show_base(self, img_info: img_info_class):
        return [
            img_info.index,
            img_info.get_img_name(),
            img_info.get_file_name(),
            img_info.get_upload_date()
        ]

    def get_all_show_base(self):
        show_base_list = []
        for img_info in self.img_info_list:
            show_base_list.append(self.get_show_base(img_info))
        return show_base_list


class Application(tk.Frame):

    def __init__(self, json_path, master=None):
        super().__init__(master)
        self.master = master
        self.json_path = json_path
        self.import_full_path = None
        self.import_skyplot_path = None
        self.temp_info_class = img_info_class()
        self.info_list_class = img_list_json_class()
        self.info_list_class.load_json(self.json_path)
        self.init_interface(self.master)

    def reset_image_list(self, master, prefix=False):
        if prefix:
            self.Frame_image_list.destroy()
        self.Frame_image_list = tk.Frame(master)
        self.Frame_image_list.grid(row=0, column=0, padx=10, pady=10)
        self.init_image_list(self.Frame_image_list)

    def init_interface(self, master):

        self.reset_image_list(master)
        self.Frame_button = tk.Frame(master)
        self.Frame_button.grid(row=1, column=0, padx=10, pady=0)
        self.init_button(self.Frame_button)

        self.Frame_info_window = tk.Frame(master, bd=2, relief='groove')
        self.Frame_info_window.grid(row=2, column=0, padx=10, pady=10)
        self.init_info_window(self.Frame_info_window)

        self.Frame_image_preview = tk.Frame(master)
        self.Frame_image_preview.grid(row=0,
                                      column=1,
                                      rowspan=3,
                                      padx=10,
                                      pady=10,
                                      sticky=N + S + W + E)
        # self.init_image_preview(self.Frame_image_preview)

    def init_button(self, master):
        '''添加、删除按钮'''
        self.Button0 = tk.Button(master,
                                 text='添加',
                                 command=lambda: self.reset_info(mode='add'))
        self.Button0.grid(row=0, column=0, padx=10)

        self.Button2 = tk.Button(master, text='删除', command=self.delete_item)
        self.Button2.grid(row=0, column=1, padx=10)

    def init_image_list(self, master):
        '''表格初始化'''
        table_row = 15
        table_column = 10
        self.table = ttk.Treeview(master,
                                  height=table_row,
                                  selectmode='browse')
        self.table.grid(rowspan=table_row,
                        columnspan=table_column,
                        padx=30,
                        pady=10)

        self.vsb = ttk.Scrollbar(master,
                                 orient='vertical',
                                 command=self.table.yview)
        self.vsb.grid(rowspan=table_row,
                      row=0,
                      column=table_column + 1,
                      sticky=N + S)

        # 定义列名
        self.table['columns'] = ['image_name', 'file_name', 'upload_date']

        for data in self.info_list_class.get_all_show_base():
            self.table.insert('', 'end', text=data[0], value=data[1:])

        # 设置列标题
        self.table.heading('#0', text='序号', anchor='w')
        self.table.heading('image_name', text='图片名称')
        self.table.heading('file_name', text='文件名')
        self.table.heading('upload_date', text='添加日期')
        # 设置列宽
        self.table.column('#0', width=50)
        self.table.column('image_name', width=200, anchor='center')
        self.table.column('file_name', width=200, anchor='center')
        self.table.column('upload_date', width=200, anchor='center')

        self.table.bind('<<TreeviewSelect>>', self.img_selection_callback)

    def init_info_window(self, master, prefix=False):
        '''信息窗口初始化'''

        def import_img_file(target):
            '''导入图片文件窗口'''

            def submit_img(target):
                '''提交文件路径'''

                def validate_import_img():
                    '''验证图片文件路径是否正确'''

                    img_path = self.entry_img_import_top_bind.get().strip()
                    if img_path == '':
                        messagebox.showerror('错误', '图片路径不能为空')
                        return False

                    if not os.path.exists(img_path):
                        messagebox.showerror('错误', '图片文件不存在')
                        return False
                    if not img_path.lower().endswith(
                        ('.jpg', '.jpeg', '.png', '.bmp')):
                        messagebox.showerror('错误', '不支持该图片格式')
                        return False
                    return True

                valid = validate_import_img()
                if valid:

                    match target:
                        case 'full':

                            self.import_full_path = self.entry_img_import_top_bind.get(
                            ).strip()
                            show_temp_path = '/masterpiece/full/full_' + os.path.basename(
                                self.import_full_path)
                            self.entry_file_path_bind.set(show_temp_path)
                        case 'skyplot':
                            self.import_skyplot_path = self.entry_img_import_top_bind.get(
                            ).strip()
                            show_temp_path = '/masterpiece/skyplot/skyplot_' + os.path.basename(
                                self.import_skyplot_path)
                            self.entry_skyplot_path_bind.set(show_temp_path)

                    self.img_import_top_window.destroy()
                else:
                    self.entry_img_import_top_bind.set('')

            x, y = self.master.winfo_rootx(), self.master.winfo_rooty()

            self.img_import_top_window = tk.Toplevel(self.master)

            self.img_import_top_window.geometry('+%d+%d' % (x, y + 30))
            self.img_import_top_window.grab_set()
            match target:
                case 'full':
                    self.img_import_top_window.title('导入图片')
                    self.Label_img_import = tk.Label(
                        self.img_import_top_window, text='图片路径')
                case 'skyplot':
                    self.img_import_top_window.title('导入天区图')
                    self.Label_img_import = tk.Label(
                        self.img_import_top_window, text='天区图路径')

            self.Label_img_import.grid(row=0, column=0, padx=10)

            self.entry_img_import_top_bind = tk.StringVar()
            self.entry_img_import = tk.Entry(
                self.img_import_top_window,
                textvariable=self.entry_img_import_top_bind,
                width=60)
            self.entry_img_import.grid(row=0, column=1, columnspan=3, sticky=E)

            self.entry_dialog = tk.Button(
                self.img_import_top_window,
                text='...',
                command=lambda: self.entry_img_import_top_bind.set(
                    filedialog.askopenfilename()))
            self.entry_dialog.grid(row=0, column=4, sticky=W)

            self.button_img_import_submit = tk.Button(
                self.img_import_top_window,
                text='确定',
                command=lambda: submit_img(target))
            self.button_img_import_submit.grid(row=1, column=4, sticky=W)

        def init_file_base(master):
            '''显示图片文件信息'''
            self.Label_img_name = tk.Label(master, text='图片名称')
            self.Label_img_name.grid(row=0, column=0, padx=10, sticky=E)

            self.entry_img_name_bind = tk.StringVar()
            self.entry_img_name = tk.Entry(
                master, textvariable=self.entry_img_name_bind)
            self.entry_img_name.grid(row=0, column=1, padx=10, sticky=W)

            self.Label_file_name = tk.Label(master, text='目标文件名')
            self.Label_file_name.grid(row=0, column=2, padx=10, sticky=E)

            self.entry_file_name_bind = tk.StringVar()
            self.entry_file_name = tk.Entry(
                master, textvariable=self.entry_file_name_bind)
            self.entry_file_name.grid(row=0, column=3, padx=10, sticky=W)

            self.entry_file_name.bind('<KeyRelease>',
                                      self.update_file_name_to_path_callback)

            self.Label_file_path = tk.Label(master, text='图片路径')
            self.Label_file_path.grid(row=1, column=0, padx=10)

            self.entry_file_path_bind = tk.StringVar()
            self.entry_file_path = tk.Label(
                master,
                textvariable=self.entry_file_path_bind,
                width=60,
                bd=2,
                relief='groove',
                anchor=W)
            self.entry_file_path.grid(row=1, column=1, columnspan=3, sticky=E)

            self.button_img_import = tk.Button(
                master, text='导入图片', command=lambda: import_img_file('full'))
            self.button_img_import.grid(row=1, column=4, sticky=W)

            self.Label_skyplot_path = tk.Label(master, text='天区图路径')
            self.Label_skyplot_path.grid(row=2, column=0, padx=10)

            self.entry_skyplot_path_bind = tk.StringVar()
            self.entry_skyplot_path = tk.Label(
                master,
                textvariable=self.entry_skyplot_path_bind,
                width=60,
                bd=2,
                relief='groove',
                anchor=W)
            self.entry_skyplot_path.grid(row=2,
                                         column=1,
                                         columnspan=3,
                                         sticky=E)

            self.button_skyplot_path = tk.Button(
                master,
                text='导入天区图',
                command=lambda: import_img_file('skyplot'))
            self.button_skyplot_path.grid(row=2, column=4, sticky=W)

        def init_base_info(master):
            '''显示基本信息'''

            def init_update_date(master, prefix):
                '''上传日期'''

                def update_date_popup():
                    '''日期弹出窗口'''

                    def update_date():
                        self.entry_upload_date_bind.set(
                            self.cal_update.get_date())
                        self.cal_update_top.destroy()

                    x, y = self.calendar_upload_date.winfo_rootx(
                    ), self.calendar_upload_date.winfo_rooty()
                    self.cal_update_top = tk.Toplevel(self.master)
                    self.cal_update_top.title('选择日期')
                    self.cal_update_top.geometry('+%d+%d' % (x, y + 30))
                    self.cal_update_top.grab_set()
                    self.cal_update = Calendar(self.cal_update_top,
                                               selectmode='day',
                                               date_pattern='y年m月d日')
                    self.cal_update.grid()
                    self.cal_update_submit_button = tk.Button(
                        self.cal_update_top, text='确定', command=update_date)
                    self.cal_update_submit_button.grid()

                self.entry_upload_date_bind = tk.StringVar()
                if prefix:
                    self.entry_upload_date_bind.set(
                        Calendar(master, date_pattern='y年m月d日').get_date())
                self.entry_upload_date = tk.Entry(
                    master, textvariable=self.entry_upload_date_bind)
                self.entry_upload_date.grid(row=0, column=0, padx=0)

                self.calendar_upload_date = tk.Button(
                    master, text='...', command=update_date_popup)
                self.calendar_upload_date.grid(row=0, column=1, padx=0)

            self.Label_photographer = tk.Label(master, text='作者（们）')
            self.Label_photographer.grid(row=0, column=0, padx=10)

            self.entry_photographer_bind = tk.StringVar()
            self.entry_photographer = tk.Entry(
                master, textvariable=self.entry_photographer_bind)
            self.entry_photographer.grid(row=0, column=1, padx=10, sticky=W)

            self.Label_target_name = tk.Label(master, text='目标名称')
            self.Label_target_name.grid(row=1, column=0, padx=10)

            self.entry_target_name_bind = tk.StringVar()
            self.entry_target_name = tk.Entry(
                master, textvariable=self.entry_target_name_bind)
            self.entry_target_name.grid(row=2, column=1, padx=10, sticky=W)

            self.Label_skyplot = tk.Label(master, text='天区位置')
            self.Label_skyplot.grid(row=2, column=0, padx=10)

            self.entry_skyplot_bind = tk.StringVar()
            self.entry_skyplot = tk.Entry(master,
                                          textvariable=self.entry_skyplot_bind)
            self.entry_skyplot.grid(row=1, column=1, padx=10, sticky=W)

            self.Label_upload_date = tk.Label(master, text='添加日期')
            self.Label_upload_date.grid(row=3, column=0, padx=10)

            self.Frame_upload_date = tk.Frame(master)
            self.Frame_upload_date.grid(row=3, column=1, padx=10, sticky=W)
            init_update_date(self.Frame_upload_date, prefix=prefix)

            self.Label_image_description = tk.Label(master, text='图片描述')
            self.Label_image_description.grid(row=4, column=0, padx=10)

            self.entry_image_description = tk.Text(master, width=25, height=5)
            self.entry_image_description.grid(row=4,
                                              column=1,
                                              padx=10,
                                              sticky=W)

        def init_shoot_info(master):
            '''显示拍摄信息'''
            self.Label_shoot_date = tk.Label(master, text='拍摄日期')
            self.Label_shoot_date.grid(row=0, column=0, padx=10)

            self.entry_shoot_date = tk.Text(master, width=25, height=3)
            self.entry_shoot_date.grid(row=0, column=1, padx=10, sticky=W)

            self.Label_location = tk.Label(master, text='拍摄地点')
            self.Label_location.grid(row=1, column=0, padx=10)

            self.entry_location_bind = tk.StringVar()
            self.entry_location = tk.Entry(
                master, textvariable=self.entry_location_bind, width=25)
            self.entry_location.grid(row=1, column=1, padx=10, sticky=W)

            self.Label_exposure = tk.Label(master, text='曝光时间')
            self.Label_exposure.grid(row=2, column=0, padx=10)

            self.entry_exposure = tk.Text(master, width=25, height=5)
            self.entry_exposure.grid(row=2, column=1, padx=10, sticky=W)

        def init_equipment_info(master):
            '''显示设备信息'''
            self.Label_telescope = tk.Label(master, text='望远镜')
            self.Label_telescope.grid(row=0, column=0, padx=10)

            self.entry_telescope_bind = tk.StringVar()
            self.entry_telescope = tk.Entry(
                master, textvariable=self.entry_telescope_bind, width=26)
            self.entry_telescope.grid(row=0, column=1, padx=10, sticky=W)

            self.Label_camera = tk.Label(master, text='相机')
            self.Label_camera.grid(row=1, column=0, padx=10, sticky=W)

            self.entry_camera_bind = tk.StringVar()
            self.entry_camera = tk.Entry(master,
                                         textvariable=self.entry_camera_bind,
                                         width=26)
            self.entry_camera.grid(row=1, column=1, padx=10, sticky=W)

            self.Label_mount = tk.Label(master, text='底座')
            self.Label_mount.grid(row=2, column=0, padx=10, sticky=W)

            self.entry_mount_bind = tk.StringVar()
            self.entry_mount = tk.Entry(master,
                                        textvariable=self.entry_mount_bind,
                                        width=26)
            self.entry_mount.grid(row=2, column=1, padx=10, sticky=W)

            self.Label_filter = tk.Label(master, text='滤镜')
            self.Label_filter.grid(row=3, column=0, padx=10)

            self.entry_filter_bind = tk.StringVar()
            self.entry_filter = tk.Entry(master,
                                         textvariable=self.entry_filter_bind,
                                         width=26)
            self.entry_filter.grid(row=3, column=1, padx=10, sticky=W)

            self.Label_guide_camera = tk.Label(master, text='导星相机')
            self.Label_guide_camera.grid(row=4, column=0, padx=10)

            self.entry_guide_camera_bind = tk.StringVar()
            self.entry_guide_camera = tk.Entry(
                master, textvariable=self.entry_guide_camera_bind, width=26)
            self.entry_guide_camera.grid(row=4, column=1, padx=10, sticky=W)

            self.Label_focuser = tk.Label(master, text='调焦')
            self.Label_focuser.grid(row=5, column=0, padx=10, sticky=W)

            self.entry_focuser_bind = tk.StringVar()
            self.entry_focuser = tk.Entry(master,
                                          textvariable=self.entry_focuser_bind,
                                          width=26)
            self.entry_focuser.grid(row=5, column=1, padx=10, sticky=W)

            self.Label_accessory = tk.Label(master, text='附件')
            self.Label_accessory.grid(row=6, column=0, padx=10, sticky=W)

            self.entry_accessory = tk.Text(master, width=25, height=2)
            self.entry_accessory.grid(row=6, column=1, padx=10, sticky=W)

            self.Label_software = tk.Label(master, text='软件')
            self.Label_software.grid(row=7, column=0, padx=10, sticky=W)

            self.entry_software_bind = tk.StringVar()
            self.entry_software = tk.Entry(
                master, textvariable=self.entry_software_bind, width=26)
            self.entry_software.grid(row=7, column=1, padx=10, sticky=W)

        def init_advanced_info(master):
            '''显示高级信息'''

            def init_RA(master):
                '''赤经'''
                self.entry_RA_h_bind = tk.StringVar()
                self.entry_RA_h = tk.Entry(master,
                                           textvariable=self.entry_RA_h_bind,
                                           width=3)
                self.entry_RA_h.grid(row=0, column=0, padx=0)

                self.Label_RA_h = tk.Label(master, text='h', width=2)
                self.Label_RA_h.grid(row=0, column=1, padx=0)

                self.entry_RA_m_bind = tk.StringVar()
                self.entry_RA_m = tk.Entry(master,
                                           textvariable=self.entry_RA_m_bind,
                                           width=3)
                self.entry_RA_m.grid(row=0, column=2, padx=0)

                self.Label_RA_m = tk.Label(master, text='m', width=2)
                self.Label_RA_m.grid(row=0, column=3, padx=0)

                self.entry_RA_s_bind = tk.StringVar()
                self.entry_RA_s = tk.Entry(master,
                                           textvariable=self.entry_RA_s_bind,
                                           width=6)
                self.entry_RA_s.grid(row=0, column=4, padx=0)

                self.Label_RA_s = tk.Label(master, text='s', width=2)
                self.Label_RA_s.grid(row=0, column=5, padx=0)

            def init_DEC(master):
                '''赤纬'''
                self.entry_DEC_h_bind = tk.StringVar()
                self.entry_DEC_h = tk.Entry(master,
                                            textvariable=self.entry_DEC_h_bind,
                                            width=3)
                self.entry_DEC_h.grid(row=0, column=0, padx=0)

                self.Label_DEC_h = tk.Label(master, text='°', width=2)
                self.Label_DEC_h.grid(row=0, column=1, padx=0)

                self.entry_DEC_m_bind = tk.StringVar()
                self.entry_DEC_m = tk.Entry(master,
                                            textvariable=self.entry_DEC_m_bind,
                                            width=3)
                self.entry_DEC_m.grid(row=0, column=2, padx=0)

                self.Label_DEC_m = tk.Label(master, text='\'', width=2)
                self.Label_DEC_m.grid(row=0, column=3, padx=0)

                self.entry_DEC_s_bind = tk.StringVar()
                self.entry_DEC_s = tk.Entry(master,
                                            textvariable=self.entry_DEC_s_bind,
                                            width=6)
                self.entry_DEC_s.grid(row=0, column=4, padx=0)

                self.Label_DEC_s = tk.Label(master, text='\'', width=2)
                self.Label_DEC_s.grid(row=0, column=5, padx=0)

            def init_pixel_scale(master):
                '''像素分辨率'''
                self.entry_pixel_scale_bind = tk.StringVar()
                self.entry_pixel_scale = tk.Entry(
                    master, textvariable=self.entry_pixel_scale_bind, width=6)
                self.entry_pixel_scale.grid(row=0, column=0, padx=0)

                self.combo_pixel_scale = ttk.Combobox(master,
                                                      state='readonly',
                                                      width=4)
                self.combo_pixel_scale['values'] = ('"/px', '\'/px', '°/px')
                self.combo_pixel_scale.current(0)
                self.combo_pixel_scale.grid(row=0, column=1, padx=0)

            def init_FOV(master):
                '''视场大小'''
                self.entry_FOV_width_bind = tk.StringVar()
                self.entry_FOV_width = tk.Entry(
                    master, textvariable=self.entry_FOV_width_bind, width=6)
                self.entry_FOV_width.grid(row=0, column=0, padx=0)

                self.Label_FOV_plus = tk.Label(master, text='x')
                self.Label_FOV_plus.grid(row=0, column=1, padx=0)

                self.entry_FOV_height_bind = tk.StringVar()
                self.entry_FOV_height = tk.Entry(
                    master, textvariable=self.entry_FOV_height_bind, width=6)
                self.entry_FOV_height.grid(row=0, column=2, padx=0)

                self.combo_FOV = ttk.Combobox(master,
                                              state='readonly',
                                              width=1)
                self.combo_FOV['values'] = ('"', '\'', '°')
                self.combo_FOV.current(0)
                self.combo_FOV.grid(row=0, column=3, padx=0)

            self.Label_file_size = tk.Label(master, text='文件大小')
            self.Label_file_size.grid(row=0, column=0, padx=10)

            self.entry_file_size_bind = tk.StringVar()
            self.entry_file_size = tk.Label(
                master,
                textvariable=self.entry_file_size_bind,
                bd=2,
                relief='groove',
                width=15)
            self.entry_file_size.grid(row=0, column=1, padx=10, sticky=W)

            self.Label_resolution = tk.Label(master, text='分辨率')
            self.Label_resolution.grid(row=1, column=0, padx=10)

            self.entry_resolution_bind = tk.StringVar()
            self.entry_resolution = tk.Label(
                master,
                textvariable=self.entry_resolution_bind,
                bd=2,
                relief='groove',
                width=15)
            self.entry_resolution.grid(row=1, column=1, padx=10, sticky=W)

            self.Label_RA = tk.Label(master, text='赤经')
            self.Label_RA.grid(row=2, column=0, padx=10)

            self.entry_RA = tk.Frame(master)
            self.entry_RA.grid(row=2, column=1, padx=10, sticky=W)

            init_RA(self.entry_RA)

            self.Label_DEC = tk.Label(master, text='赤纬')
            self.Label_DEC.grid(row=3, column=0, padx=10)

            self.entry_DEC = tk.Frame(master)
            self.entry_DEC.grid(row=3, column=1, padx=10, sticky=W)

            init_DEC(self.entry_DEC)

            self.Label_pixel_scale = tk.Label(master, text='像素分辨率')
            self.Label_pixel_scale.grid(row=4, column=0, padx=10)

            self.Frame_pixel_scale = tk.Frame(master)
            self.Frame_pixel_scale.grid(row=4, column=1, padx=10, sticky=W)

            init_pixel_scale(self.Frame_pixel_scale)

            self.Label_FOV = tk.Label(master, text='视场大小')
            self.Label_FOV.grid(row=5, column=0, padx=10)

            self.Frame_FOV = tk.Frame(master)
            self.Frame_FOV.grid(row=5, column=1, padx=10, sticky=W)

            init_FOV(self.Frame_FOV)

        def init_buton(master):
            '''保存、重置、取消按钮''' ''
            self.Button_submit = tk.Button(master,
                                           text='保存',
                                           command=self.save_data)
            self.Button_submit.grid(row=0, column=0, padx=10, pady=10)

            self.Button_reset = tk.Button(
                master,
                text='重置',
                command=lambda: self.reset_info(mode='reset'))
            self.Button_reset.grid(row=0, column=1, padx=10, pady=10)

            self.Button_cancel = tk.Button(
                master,
                text='取消',
                command=lambda: self.reset_info(mode='cancel'))
            self.Button_cancel.grid(row=0, column=2, padx=10, pady=10)

        self.Frame_file_base = tk.Frame(master)
        self.Frame_file_base.grid(row=0,
                                  column=0,
                                  columnspan=2,
                                  padx=10,
                                  pady=10)
        init_file_base(self.Frame_file_base)

        self.Frame_base_info = tk.Frame(master)
        self.Frame_base_info.grid(row=1, column=1, padx=10, pady=10)
        init_base_info(self.Frame_base_info)

        self.Frame_shoot_info = tk.Frame(master)
        self.Frame_shoot_info.grid(row=1, column=0, padx=10, pady=10)
        init_shoot_info(self.Frame_shoot_info)

        self.Frame_equipment_info = tk.Frame(master)
        self.Frame_equipment_info.grid(row=2,
                                       column=1,
                                       rowspan=2,
                                       padx=10,
                                       pady=10)
        init_equipment_info(self.Frame_equipment_info)

        self.Frame_advanced_info = tk.Frame(master)
        self.Frame_advanced_info.grid(row=2, column=0, padx=10, pady=10)
        init_advanced_info(self.Frame_advanced_info)

        if prefix:
            self.Frame_button = tk.Frame(master)
            self.Frame_button.grid(row=3, column=0, padx=10, pady=10)
            init_buton(self.Frame_button)

    def init_image_preview(self, master):
        '''图片预览'''
        self.Label_image_preview = tk.Label(master, text='图片预览')
        self.Label_image_preview.grid(row=0,
                                      column=0,
                                      padx=10,
                                      pady=10,
                                      sticky=N + S)

        self.image = Image.open(os.getcwd() +
                                self.temp_info_class.get_img_path())
        self.python_image = ImageTk.PhotoImage(self.image)
        self.Label_image_preview = ttk.Label(master, image=self.python_image)
        self.Label_image_preview.grid(row=1, column=0, padx=10, pady=10)

    def reset_info(self, mode):
        '''重置信息窗口'''
        self.Frame_info_window.destroy()
        self.Frame_info_window = tk.Frame(self.master, bd=2, relief='groove')
        self.Frame_info_window.grid(row=2, column=0, padx=10, pady=10)
        self.import_full_path = None
        self.import_skyplot_path = None

        match mode:
            case 'add':
                for i in self.table.selection():
                    self.table.selection_remove(i)
                self.init_info_window(self.Frame_info_window, True)
                self.temp_info_class.clear()

            case 'reset':
                if self.temp_info_class.index == None:
                    self.init_info_window(self.Frame_info_window, True)
                    self.temp_info_class.clear()
                else:
                    self.init_info_window(self.Frame_info_window, True)
                    self.display_info()
            case 'cancel':
                for i in self.table.selection():
                    self.table.selection_remove(i)
                self.init_info_window(self.Frame_info_window, False)
                self.temp_info_class.clear()

    def update_file_name_to_path_callback(self, event):
        '''目标文件名输入框事件'''
        widget = event.widget

        if self.entry_file_path_bind.get().strip() != '':
            temp_ext = os.path.splitext(
                self.entry_file_path_bind.get().strip())[1]

            self.entry_file_path_bind.set('/masterpiece/full/full_' +
                                          widget.get().strip() + temp_ext)

        if self.entry_skyplot_path_bind.get().strip() != '':
            temp_ext = os.path.splitext(
                self.entry_skyplot_path_bind.get().strip())[1]

            self.entry_skyplot_path_bind.set('/masterpiece/skyplot/skyplot_' +
                                             widget.get().strip() + temp_ext)

    def img_selection_callback(self, event):
        '''图片列表选择事件'''
        widget = event.widget
        if widget.selection() == ():
            return
        print('选择的是：' + str(widget.selection()))

        selected = widget.selection()[0]
        index_selected = self.table.item(selected, 'text')
        self.reset_info(mode='reset')
        self.load_list_to_temp(index_selected)
        self.display_info()

    def display_info(self):
        '''刷新显示'''
        self.entry_img_name_bind.set(self.temp_info_class.get_img_name())
        self.entry_file_name_bind.set(self.temp_info_class.get_file_name())
        self.entry_file_path_bind.set(self.temp_info_class.get_img_path())
        self.entry_skyplot_path_bind.set(
            self.temp_info_class.get_skyplot_path())
        self.entry_photographer_bind.set(
            self.temp_info_class.get_photographer())
        self.entry_target_name_bind.set(self.temp_info_class.get_target_name())
        self.entry_skyplot_bind.set(self.temp_info_class.get_skyplot())
        self.entry_upload_date_bind.set(self.temp_info_class.get_upload_date())
        self.entry_image_description.delete(1.0, 'end')
        self.entry_image_description.insert(
            'insert', self.temp_info_class.get_image_description())
        self.entry_shoot_date.delete(1.0, 'end')
        self.entry_shoot_date.insert('insert',
                                     self.temp_info_class.get_shoot_date())
        self.entry_location_bind.set(self.temp_info_class.get_location())
        self.entry_exposure.delete(1.0, 'end')
        self.entry_exposure.insert('insert',
                                   self.temp_info_class.get_exposure())
        self.entry_telescope_bind.set(self.temp_info_class.get_telescope())
        self.entry_camera_bind.set(self.temp_info_class.get_camera())
        self.entry_mount_bind.set(self.temp_info_class.get_mount())
        self.entry_filter_bind.set(self.temp_info_class.get_filter())
        self.entry_guide_camera_bind.set(
            self.temp_info_class.get_guide_camera())
        self.entry_focuser_bind.set(self.temp_info_class.get_focuser())
        self.entry_accessory.delete(1.0, 'end')
        self.entry_accessory.insert('insert',
                                    self.temp_info_class.get_accessory())
        self.entry_software_bind.set(self.temp_info_class.get_software())
        self.entry_file_size_bind.set(self.temp_info_class.get_file_size())
        self.entry_resolution_bind.set(self.temp_info_class.get_resolution())
        self.entry_RA_h_bind.set(self.temp_info_class.get_RA('h'))
        self.entry_RA_m_bind.set(self.temp_info_class.get_RA('m'))
        self.entry_RA_s_bind.set(self.temp_info_class.get_RA('s'))
        self.entry_DEC_h_bind.set(self.temp_info_class.get_DEC('d'))
        self.entry_DEC_m_bind.set(self.temp_info_class.get_DEC('m'))
        self.entry_DEC_s_bind.set(self.temp_info_class.get_DEC('s'))
        self.entry_pixel_scale_bind.set(
            self.temp_info_class.get_pixel_scale()[0])
        self.combo_pixel_scale.set(self.temp_info_class.get_pixel_scale()[1])
        self.entry_FOV_width_bind.set(self.temp_info_class.get_FOV()[0])
        self.entry_FOV_height_bind.set(self.temp_info_class.get_FOV()[1])
        self.combo_FOV.set(self.temp_info_class.get_FOV()[2])

    def save_to_temp(self):
        '''临时保存信息'''
        self.temp_info_class.set_img_name(self.entry_img_name_bind.get())
        self.temp_info_class.set_file_name(self.entry_file_name_bind.get())
        self.temp_info_class.set_img_path(self.entry_file_path_bind.get())
        self.temp_info_class.set_skyplot_path(
            self.entry_skyplot_path_bind.get())
        self.temp_info_class.set_photographer(
            self.entry_photographer_bind.get())
        self.temp_info_class.set_target_name(self.entry_target_name_bind.get())
        self.temp_info_class.set_skyplot(self.entry_skyplot_bind.get())
        self.temp_info_class.set_upload_date(self.entry_upload_date_bind.get())
        self.temp_info_class.set_image_description(
            self.entry_image_description.get('1.0', 'end'))
        self.temp_info_class.set_shoot_date(
            self.entry_shoot_date.get('1.0', 'end'))
        self.temp_info_class.set_location(self.entry_location_bind.get())
        self.temp_info_class.set_exposure(self.entry_exposure.get(
            '1.0', 'end'))
        self.temp_info_class.set_telescope(self.entry_telescope_bind.get())
        self.temp_info_class.set_camera(self.entry_camera_bind.get())
        self.temp_info_class.set_mount(self.entry_mount_bind.get())
        self.temp_info_class.set_filter(self.entry_filter_bind.get())
        self.temp_info_class.set_guide_camera(
            self.entry_guide_camera_bind.get())
        self.temp_info_class.set_focuser(self.entry_focuser_bind.get())
        self.temp_info_class.set_accessory(
            self.entry_accessory.get('1.0', 'end'))
        self.temp_info_class.set_software(self.entry_software_bind.get())
        self.temp_info_class.set_file_size(self.entry_file_size_bind.get())
        self.temp_info_class.set_resolution(self.entry_resolution_bind.get())
        self.temp_info_class.set_RA(self.entry_RA_h_bind.get(),
                                    self.entry_RA_m_bind.get(),
                                    self.entry_RA_s_bind.get())
        self.temp_info_class.set_DEC(self.entry_DEC_h_bind.get(),
                                     self.entry_DEC_m_bind.get(),
                                     self.entry_DEC_s_bind.get())

        self.temp_info_class.set_pixel_scale(self.entry_pixel_scale_bind.get(),
                                             self.combo_pixel_scale.get())

        self.temp_info_class.set_FOV(self.entry_FOV_width_bind.get(),
                                     self.entry_FOV_height_bind.get(),
                                     self.combo_FOV.get())

    def delete_item(self):
        '''删除图片'''
        index = self.table.item(self.table.selection(), 'text')
        self.info_list_class.delete_img(index)
        self.reset_image_list(self.master, True)

    def validate_data(self):
        '''验证输入数据'''

        def is_legal_filename(filename):
            pattern = r'[\\/:\*\?"<>\|]'
            return not bool(re.search(pattern, filename))

        def validate_file_name():
            self.entry_file_name_bind.set(
                self.entry_file_name_bind.get().strip())
            if self.entry_file_name_bind.get() == '':
                self.window('请输入目标文件名')
                return False

            if not is_legal_filename(self.entry_file_name_bind.get()):
                self.window('文件名包含非法字符')
                return False

            file_name_list = [
                os.path.splitext(self.table.item(i, 'values')[1])[0]
                for i in self.table.get_children()
                if i != self.table.selection()[0]
            ]
            print(file_name_list)
            if self.entry_file_name_bind.get().lower() in [
                    i.lower() for i in file_name_list
            ]:
                self.window('已存在相同文件名')
                return False

            return True

        def validate_img_name():
            self.entry_img_name_bind.set(
                self.entry_img_name_bind.get().strip())
            if self.entry_img_name_bind.get() == '':
                self.window('请输入图片名称')
                return False

            img_name_list = [
                self.table.item(i, 'values')[0]
                for i in self.table.get_children()
                if i != self.table.selection()[0]
            ]
            print(img_name_list)
            if self.entry_img_name_bind.get() in [
                    i.lower() for i in img_name_list
            ]:
                self.window('已存在相同图片名称')
                return False

            return True

        def validate_file_path():
            self.entry_file_path_bind.set(
                self.entry_file_path_bind.get().strip())
            if self.entry_file_path_bind.get() == '':
                self.window('请输入图片路径')
                return False

            try:
                if not os.path.isfile(self.entry_file_path_bind.get()):
                    raise OSError
            except OSError:
                self.window('图片路径无效')
                return False

            return True

        def validate_skyplot_path():
            self.entry_skyplot_path_bind.set(
                self.entry_skyplot_path_bind.get().strip())
            if self.entry_skyplot_path_bind.get() == '':
                return True

            try:
                if not os.path.isfile(self.entry_skyplot_path_bind.get()):
                    raise OSError
            except OSError:
                messagebox.showerror('错误', '天区图路径无效')
                return False

            return True

        validate_img_name()
        validate_file_name()
        validate_file_path()
        validate_skyplot_path()

    def save_data(self):
        '''保存数据'''
        valid = self.validate_data()
        # if not valid:
        #     return
        self.import_full_path = None
        self.import_skyplot_path = None

        self.save_to_temp()
        if self.temp_info_class.index == None:
            self.temp_info_class.index = str(
                len(self.table.get_children()) + 1)
            self.info_list_class.add_img(self.temp_info_class)

            self.reset_image_list(self.master, True)
            self.table.selection_set(self.table.get_children()[-1])
        else:
            self.info_list_class.edit_img(self.temp_info_class.index,
                                          self.temp_info_class)
            self.table.item(self.table.selection(),
                            values=self.info_list_class.get_show_base(
                                self.temp_info_class)[1:])

        index_selected = self.table.item(self.table.selection(), 'text')

        self.load_list_to_temp(index_selected)
        self.display_info()

        # self.info_list_class.save_to_json()
    def load_list_to_temp(self, index):
        '''加载列表到临时信息'''
        self.temp_info_class = self.info_list_class.get_img(index)

    def window(self, text):
        '''创建弹窗'''
        messagebox.showinfo('提示', text)


def get_file_size(path):
    '''获取文件大小'''
    size_unit = ['B', 'KB', 'MB', 'GB']
    size = os.path.getsize(path)
    for i in range(len(size_unit)):
        if size < 1024:
            break
        size /= 1024

    if size < 10:
        size = round(size, 2)
    elif size < 100:
        size = round(size, 1)
    else:
        size = round(size)

    return str(size) + size_unit[i]


def get_resolution(path):
    '''获取分辨率'''
    with Image.open(path) as img:
        width, height = img.size
    return str(width) + 'x' + str(height)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('图片信息管理')
    root.geometry('1600x960')
    app = Application('masterpiece/image_information.json', root)
    root.mainloop()
