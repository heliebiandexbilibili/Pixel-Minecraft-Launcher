import tkinter as tk
import tkinter.ttk as ttk
import minecraft_launcher_lib as mll
import os
import time
import tkintertools
import tkinter.messagebox as messagebox
import tkinter.colorchooser
import tkinter.filedialog
import shutil
import subprocess
import threading

class MinecraftLauncher:
    def checkfiles(self):
        if os.path.isdir("./PML"):
            ddd = open("./PML/ddd.ico", "wb")
            ddd.write(b'\x00\x00\x01\x00\x01\x00\x80\x80\x00\x00\x00\x00\x00\x00\xed\x04\x00\x00\x16\x00\x00\x00\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x80\x00\x00\x00\x80\x08\x06\x00\x00\x00\xc3>a\xcb\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x04\xa7IDATx^\xed\x9d\xdbu\x141\x10D\xdbA8\t\x1f\x82\x80\x1cx\x84\x03\x84\xc3#\x07 \t\x82\xc0A\x80\xc7\xc7\x87\x0f{\x17WQ#\x8dV\xba\xfb\xdd-\xa9\xab\xaez4\xb3\xb3\xf6U\xf1YZ\x81\xab\xa5\xab\xa7\xf8\x02\x80\xc5!\x00\x00\x00X\\\x81\xc5\xcb\xa7\x03\x00\xc0\xe2\n,^>\x1d\x00\x00\x16W`\xf1\xf2\xe9\x00\x00\xb0\xb8\x02\x8b\x97O\x07\x00\x80\xc5\x15X\xbc|:\x00\x00,\xae\xc0\xe2\xe5\xd3\x01\x00 V\xe0w<\x02\x03$\nD\x9b8J~X5\x00$\xf6\xe5\xb9\x91\x87Q2\x00\xe4\xee\xed0B\xe4a\x94\x0c\x00;\xd8\x97\x0f\x11y\x18%\x03@\xee\xde\x0e#D\x1eF\xc9\x00\xb0\x83}\xf9\x10\x91\x87Q2\x00\xe4\xee\xed0B\xe4a\x94\x0c\x00;\xd8\x97\x0f\x11y\x18%\x03@\xee\xde\x0e#D\x1eF\xc9\x00\xb0\x83}\xf9\x10\x91\x87Q\xb2\t\xc0mU\xfd\xcc\xeb]b\x84\x9b\xaa\xba\x16+\x8d<\x8c\x92M\x00\xbe\xdc\x01\xf0V,j\xf5\xb0M\xab\xd7\xa2\x08\x91\x87Q2\x00\x88\x16\xf9a\x00\xe0k6U\x06\x00Le\xa7_\x0c\x00\xf8\x9aM\x95\x01\x00S\xd9\xe9\x17\x03\x00\xbefSe\x00\xc0Tv\xfa\xc5\x00\x80\xaf\xd9T\x19\x000\x95\x9d~1S\x02\xf0\xb9\xaa\xde\x89Z\xbc\xaf\xaaWbl\x8b\xb0m\xfe\x1f-\x06\x16\xc7\xfcd<5\x8d\x1e\xe6E\xc9\r\x9f\x04:;@\xd4\xd4\n\xdb\x1eYok8\xea\xe3\xd4\x1fy\x18%\x03@3>\x00\xc0\xf82\xa4\x85\x0bt\x00CU\xf5w\x01\xce\xb7\x81\xce\x0e0\x96*\x87\x02\x80,U\x15\x00\x18b\x89\xa1\xce\x06\x88.\xe3Q2g\x00\xd1N?\x0c\x008\x03\xac\xfdB\x88\xb3\x03\xfc\xfd\xf5|\x06g\x80\xe75\xfa\x1b\xc1\x19\xc0\x10K\x0cu6@t\x19\x8f\x929\x03\x88v\xfaa\x00`\x9c\x01T\x88\xb7\xb6\xbe=bU>\\\x02\x14\x95\x06\xe9\x00\x00`\x98\xf58T\x15\xef_S\x1c}\x06Pk\xa0\x03\x9cpQ\x15\x0f\x00\x82]\xf6\x1f\xa9\x9c\x018\x03\xf0\x1c`\xef_\xc6p\t\xe0\x12\xc0]\x00\x87@\xed\x82\xccm\xa0\xa6\xd3}\x14w\x01\x86Xb(\x87@\x0e\x81\xf3\x1d\x02\x9d\x97B\x9d\x97"\xd5\x97G_\xdeu\xab\xedeO\xe5\xf3\xa6\xaa\xbe*\x81U\xb5\x8d\xab|~\x19\x7f\x1f\xc1\xa9?\xba\x95\x8f\x92\x07y\x12\xa8\x88\xef\xc68g\x80K\xb9\x04\x9e\xd4\x00\x00N\xa3\x01\x00\xc6\x969z\x07\x18K\x95C\x01@\x96\xea\xf8\xbb\x00c\xa9r(\x00\xc8R\x01\xc0\xd1\x1d0\xba\x8cG\xc9\x1c\x02/\xea9\x08\x87@\xa3\xabq\t0\xc4:\xba\x05\x1aK\x95C\x01@\x96\x8a3\xc0\xd1\x1b \xba\x8cG\xc9\x9c\x018\x03l\n\xa8;\xe0\xe8G\xc1FS\xbb\x7f\x0e\xffBL\xf8 \xc6\xf1(\xd8\xf8\xa3\x07\xdd\xbe\r;c\xde2\xf3\xcfp\t\xd8\xa3\x86\xc7\x1c\x00\x80\xd8\xd6\x9cK@\xab\x9f\x87\x03\x80a\xd6\xe3\xd0=\xc4S\xcf\x00\x00\xa0\x1b\xd5\xad\x03\x01\xc0iS\xba\x19p\xf4\x19\x04\x00\x00@\xefKg"\xb9\x04\xc4\x12>\x19\xa0[\x07\xa2\x03\xd0\x01b|\xe9\x00\xb1\x84t\x80e\xef\xc39\x04\xee\xbf{\xce\x8d\xd8\xea\xa7a\x17\xdd\x01G=\x03\xb4\xc0\x02\x00N\xa8\n\x00\xa7Q\xe3}\x00c\x0b\xb6h\x81\xc6\xf4r(\x1d\x80\x0e\xd0\xe4\xd7\xc1-6\xc0\xf2\xcf\x01\xe4mm\x04\xd2\x01\xe8\x00t\x80K\xf96\xd0\xd8\xd8r(\x1d\x80\x0e@\x07\xa0\x03h\r\x83\xdb@M\xa7\xfb(\xf5\x14\xec\xbc\x14jL/\x87n\xbf\xe3W_\xe0t\xfei\xd4wq\x05\xdf\xaa\xea\xa3\x18\xbb\xfc\xdf\x07\x10u\x9a6\x8c\xdb\xc0i\xad\xd5\n\x03\x00M\xa7i\xa3\x00`Zk\xb5\xc2\x00@\xd3i\xda(\x00\x98\xd6Z\xad0\x00\xd0t\x9a6\n\x00\xa6\xb5V+\x0c\x004\x9d\xa6\x8d\x02\x80i\xad\xd5\n\x9b\x12\x80[\xe3O\xa5j2\xcd\x1buSU\xd7by\xd1k}Q\xf2\xc3\x02\xd5\xef\x02\xc4z\x083\x15\x88<\x8c\x92\x01\xc0\xb4\xaaMx\xe4a\x94\x0c\x00m\x1c5G\x8d<\x8c\x92\x01\xc0\xb4\xaaMx\xe4a\x94\x0c\x00m\x1c5G\x8d<\x8c\x92\x01\xc0\xb4\xaaMx\xe4a\x94\x0c\x00m\x1c5G\x8d<\x8c\x92\x01\xc0\xb4\xaaMx\xe4a\x94\x0c\x00m\x1c5G\x8d<\x8c\x92\x01\xc0\xb4\xaaMx\xe4a\x94\xdc\xa6\x1eF\xed\xa9\x00\x00\xf4T{\xc0\xb9\x00`@Sz.\t\x00z\xaa=\xe0\\\x000\xa0)=\x97\x04\x00=\xd5\x1ep.\x00\x18\xd0\x94\x9eK\x02\x80\x9ej\x0f8\x17\x00\x0chJ\xcf%\x01@O\xb5\x07\x9c\x0b\x00\x064\xa5\xe7\x92\x00\xa0\xa7\xda\x03\xce\x05\x00\x03\x9a\xd2sI\x00\xd0S\xed\x01\xe7\x02\x80\x01M\xe9\xb9$\x00\xe8\xa9\xf6\x80s\xfd\x01\x1d\x94\x9d\x90\xcch\xf3&\x00\x00\x00\x00IEND\xaeB`\x82')
            ddd.close()
            if not os.path.exists("./PML/PML.config") or (open("./PML/PML.config").read() == "" or open("./PML/PML.config").read().isspace()):
                with open("./PML/PML.config", "w") as f:
                    f.write('UsernameList = []\n'
                            'alpha = 0.85\n'
                            'ServerList = []\n'
                            'Backgroud = ""\n'
                            'ServerPath = []\n'
                            'LastDict = ""\n'
                            'LastLaunch = ""\n'
                            'LastUsername = ""')
        else:
            os.mkdir("PML")
            self.checkfiles()
    
    def read_configs(self):
        with open("./PML/PML.config") as f:
            for i in f.read().split("\n"):
                if i.startswith("LastDict = "):
                    self.minecraft_dir = i[12:-1]
        with open("./PML/PML.config") as f:
            for i in f.read().split("\n"):
                if i.startswith("LastLaunch = "):
                    self.selected_version = i[14:-1]
        with open("./PML/PML.config") as f:
            for i in f.read().split("\n"):
                if i.startswith("LastUsername = "):
                    self.Username = i[16:-1]
        with open("./PML/PML.config") as f:
            for i in f.read().split("\n"):
                if i.startswith("UsernameList = "):
                    self.UsernameList = i[16:-1].split(", ")
                    for i in self.UsernameList:
                        self.UsernameList[self.UsernameList.index(i)] = i[1:-1]
        with open("./PML/PML.config") as f:
            for i in f.read().split("\n"):
                if i.startswith("ServerList = "):
                    self.ServerList = i[14:-1].split(", ")
                    for i in self.ServerList:
                        self.ServerList[self.ServerList.index(i)] = i[1:-1]
        with open("./PML/PML.config") as f:
            for i in f.read().split("\n"):
                if i.startswith("Background = "):
                    if i[13:] != '""':
                        self.bg = i[13:]                        
        with open("./PML/PML.config") as f:
            for i in f.read().split("\n"):
                if i.startswith("ServerPath = "):
                    for j in i[14:-1].split(", "):
                        self.ServerPath.append(j)
    
    def init_var(self):
        self.UsernameList = []
        self.ServerList = []
        self.ServerPath = []
        self.minecraft_dir = ""
        self.selected_version = ""
        self.Username = ""
        self.bg = None
        self.support_mod = False
        self.modlistlist = []
        self.read_configs()
        self.current_max = 0
        self.downloaded_minecraft_versions = os.listdir(os.path.join(self.minecraft_dir, "versions"))
        self.download_version_to = ''
        self.support_fabric = ""
        self.support_forge = ""

    def __init__(self):
        self.checkfiles()
        self.main_win = tk.Tk()
        self.main_win.title("Pixel Minecraft Launcher")
        self.main_win.geometry("1150x650")
        self.alpha = float(open("./PML/PML.config").read().split("\n")[1].split(" ")[-1])
        self.main_win.attributes('-alpha',self.alpha)
        self.main_win.resizable(False, False)
        self.main_win.iconbitmap("PML/ddd.ico")
        self.init_var()
        #欢迎标题
        self.main_win.config(bg=self.bg)
        self.Label = tk.Label(self.main_win, text=f"欢迎回来，{os.getlogin()}", font=("等线", 15), bg=self.bg)
        self.Label.place(x=15, y=610)
        #启动游戏标语&按钮
        self.Start_Game_Label = tk.Label(self.main_win, text=f"是时候启动游戏了！\n正在使用的账户:{self.Username}\n准备启动游戏:{self.selected_version}", bg=self.bg)
        self.Start_Game_Label.place(x=900, y=500)
        self.Start_Game_Button = tk.Button(self.main_win, text="启动游戏", width=30, height=2, relief="ridge", command=self.start_th)
        self.Start_Game_Button.place(x=880, y=560)
        self.create_main()

        self.main_win.mainloop()
    
    def delete_main(self):
        self.Others_Button.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.ServerLauncher_Button.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.Settings_Button.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.Download_Button.destroy()
        time.sleep(0.06)
        self.Modify_Button.destroy()
        self.main_win.update()
    
    def start_th(self): threading.Thread(target=self.start_game).start()
    
    def create_main(self):
        self.Modify_Button = tk.Button(self.main_win, text="版本选择&版本设置", width=30, height=1, relief="ridge", command=self.change_version_and_modify_version)
        self.Modify_Button.place(x=880, y=700)
        tkintertools.Animation(self.Modify_Button, 250, translation=(0, -90), fps=90).run()
        # 开始写控件类
        self.Download_Button = tk.Button(self.main_win, text="下载版本", width=20, height=25, command=self.from_menu_to_download_page, anchor="se", font=("等线"), relief="groove")
        self.Download_Button.place(x=170, y=200)
        tkintertools.Animation(self.Download_Button, translation=(0, -150), ms=250).run()
        self.Settings_Button = tk.Button(self.main_win, text="用户设置", width=20, height=25, command=self.from_menu_to_user_settigs_page, anchor="se", font=("等线"), relief="groove")
        self.Settings_Button.place(x=370, y=-200)
        tkintertools.Animation(self.Settings_Button, translation=(0, 250), ms=250).run()
        self.ServerLauncher_Button = tk.Button(self.main_win, text="服务器启动", width=20, height=25, anchor="se", font=("等线"), relief="groove", command=self.from_menu_to_server_page)
        self.ServerLauncher_Button.place(x=570, y=200)
        tkintertools.Animation(self.ServerLauncher_Button, translation=(0, -150), ms=250).run()
        self.Others_Button = tk.Button(self.main_win, text="杂项设置", width=20, height=25, anchor="se", font=("等线"), relief="groove", command=self.from_menu_to_PML_settings_page)
        self.Others_Button.place(x=770, y=-200)
        tkintertools.Animation(self.Others_Button, translation=(0, 250), ms=250).run()
    
    def set_alpha(self, value):
        self.main_win.attributes("-alpha", self.scale.get()/100)
        self.alpha = self.scale.get()/100
        self.save_all()

    def get_version_list(self):
        return mll.utils.get_version_list()
    
    def delete_download(self):
        self.Menu_Butt.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.VersionDescription.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.version_listbox.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.VersionDescriptionLabel.destroy()
        self.main_win.update()
        self.create_main()
    
    def delete_modify(self):
        self.Menu_Butt.destroy()
        self.VersionListListBox.destroy()
        self.VerDescription.destroy()
        self.Change_Dir.destroy()
        self.VerDescriptionLabel.destroy()
        self.modlist.destroy()
        self.ModListListBox.destroy()
        self.supply_mod_loading.destroy()
        self.Add_Mod.destroy()
        self.Delete_Mod.destroy()
        self.d_mod.destroy()
        self.e_mod.destroy()
        self.main_win.update()
        self.create_main()

    def delete_mod(self):
        if self.ModListListBox.curselection() != ():
            os.remove(f"{self.minecraft_dir}/versions/{self.selected_version}/mods/{self.modlistlist[self.ModListListBox.curselection()[0]]}")
            del self.modlistlist[self.ModListListBox.curselection()[0]]
            tkinter.messagebox.showinfo("成功", f"已删除1个mod:{self.ModListListBox.get('active')}")
            self.ModListListBox.delete("active")

    def reload_mods(self):
        self.ModListListBox.delete(0, tk.END)
        self.modlistlist = []
        if self.support_mod and self.selected_version != "":
            for i in os.listdir(f"{self.minecraft_dir}/versions/{self.selected_version}/mods"):
                self.modlistlist.append(i)
                if i.endswith(".disabled"):
                    self.ModListListBox.insert(tk.END, i[:-9] + "(已被禁用)")
                else:
                    self.ModListListBox.insert(tk.END, i)
        else:
            self.ModListListBox.insert(tk.END, "您的版本并不支持mod或者没有选中版本")
    
    def start_game(self):
        callback = {
            "setStatus": self.set_status,
            "setProgress": self.set_progress,
            "setMax": self.set_max
        }
        options = {
            "username": self.Username,
            "-Dminecraft.launcher.brand": "PML Launcher",
            "-Dminecraft.launcher.version": "4.0",
            "--accessToken": "",
            "--userType": "Legacy"
        }
        minecraft_command = mll.command.get_minecraft_command(
            self.selected_version, self.minecraft_dir, options)
        subprocess.call(minecraft_command)
    
    def add_mod(self):
        modplace = tk.filedialog.askopenfilename(title="打开mod位置")
        if modplace != "" and self.support_mod:
            shutil.copy(modplace, f"{self.minecraft_dir}/versions/{self.selected_version}/mods/{os.path.basename(modplace)}")
            tkinter.messagebox.showinfo("成功", f"已成功安装{os.path.basename(modplace)}到{self.selected_version}")
            self.reload_mods()
    
    def is_disabled(self):
        if self.ModListListBox.curselection != ():
            return self.modlistlist[self.ModListListBox.curselection()[0]].endswith(".disabled")

    def disable_mod(self):
        if not self.is_disabled():
            os.rename(f"{self.minecraft_dir}/versions/{self.selected_version}/mods/{self.modlistlist[self.ModListListBox.curselection()[0]]}", f"{self.minecraft_dir}/versions/{self.selected_version}/mods/{self.modlistlist[self.ModListListBox.curselection()[0]]}.disabled")
            self.reload_mods()

    def enable_mod(self):
        if self.is_disabled():
            os.rename(f"{self.minecraft_dir}/versions/{self.selected_version}/mods/{self.modlistlist[self.ModListListBox.curselection()[0]]}", f"{self.minecraft_dir}/versions/{self.selected_version}/mods/{self.modlistlist[self.ModListListBox.curselection()[0]][:-9]}")
            self.reload_mods()
    
    def UpdateModListAndUpdateModLoaderSupport(self, *args):
        if self.VersionListListBox.curselection() != ():
            self.selected_version = self.VersionListListBox.get(self.VersionListListBox.curselection()[0])
            if len(self.selected_version) >= len("1.20.3 Fabric 0.16.2"):
                self.Start_Game_Label.config(text=f"是时候启动游戏了！\n正在使用的账户:{self.Username}\n准备启动游戏:{self.selected_version[:19]}\n{self.selected_version[19:]}")
                self.Start_Game_Label.place(x=900, y=483)
            else:
                self.Start_Game_Label.config(text=f"是时候启动游戏了！\n正在使用的账户:{self.Username}\n准备启动游戏:{self.selected_version}")
                self.Start_Game_Label.place(x=900, y=500)
            try:
                for i in os.listdir(f"{self.minecraft_dir}/versions/{self.selected_version}"):
                    if i.endswith(".json"):
                        self.support_mod = True if "forge" in open(f"{self.minecraft_dir}/versions/{self.selected_version}/{i}").read() or "fabric" in open(f"{self.minecraft_dir}/versions/{self.selected_version}/{i}").read() else False
                        self.supply_mod_loading.config(text="支持mod加载:支持" if self.support_mod else "支持mod加载:不支持")
                        break
                self.reload_mods()
            except FileNotFoundError:
                pass

    def download_minecraft_version_theard(self):
        t1 = threading.Thread(target=self.download_version).start()
        self.download_task_list.append(t1)
        print("成功创建下载任务:", self.download_version_to)
            
    def change_version_and_modify_version(self):
        self.delete_main()
        self.Menu_Butt = tk.Button(self.main_win, text="🏠", command=self.delete_modify)
        self.Menu_Butt.place(x=0, y=0)
        self.Change_Dir = tk.Button(self.main_win, text="🔄️", command=self.change_minecraft_dir)
        self.Change_Dir.place(x=0, y=30)
        self.VersionListListBox = tk.Listbox(self.main_win, width=40, height=25)
        self.VersionListListBox.place(x=30, y=0)
        for i in self.downloaded_minecraft_versions:
            if i != "" and not i.isspace():
                self.VersionListListBox.insert(0, i)
        self.VerDescription = ttk.Frame(self.main_win, width=750, height=454, relief="ridge")
        self.VerDescription.place(x=350, y=0)
        self.VerDescriptionLabel = tk.Label(self.VerDescription, text="版本信息", font=("等线", 25))
        self.VerDescriptionLabel.place(x=20, y=0)
        self.supply_mod_loading = tk.Label(self.VerDescription, text="支持mod加载:")
        self.supply_mod_loading.place(x=20, y=60)      
        self.VersionListListBox.bind("<<ListboxSelect>>", self.UpdateModListAndUpdateModLoaderSupport)
        self.modlist = tk.Label(self.VerDescription, text="Mod列表")
        self.modlist.place(x=10, y=80)
        self.Add_Mod = tk.Button(self.VerDescription, text="➕", command=self.add_mod)
        self.Add_Mod.place(x=10, y=100)
        self.Delete_Mod = tk.Button(self.VerDescription, text="➖", command=self.delete_mod)
        self.Delete_Mod.place(x=10, y=135)
        self.d_mod = tk.Button(self.VerDescription, text="🚫", command=self.disable_mod)
        self.d_mod.place(x=10, y=170)
        self.e_mod = tk.Button(self.VerDescription, text="☑️", command=self.enable_mod)
        self.e_mod.place(x=10, y=205)
        self.ModListListBox = tk.Listbox(self.VerDescription, width=50, height=19)
        self.ModListListBox.place(x=36, y=100) 

    def delete_PML_settings(self):
        self.Menu_Butt.destroy()
        self.scale.destroy()
        self.ColorSetLabel.destroy()
        self.ColorChooser.destroy()
        self.create_main()
    
    def set_color(self):
        color = tkinter.colorchooser.askcolor(title="设置背景颜色")
        self.main_win.config(bg=color[1])
        self.Label.config(bg=color[1])
        self.Start_Game_Label.config(bg=color[1])
        self.ColorSetLabel.config(bg=color[1])
        self.scale.config(bg=color[1])
        self.bg = color[1]
        self.save_all()
    
    def from_menu_to_PML_settings_page(self):
        self.delete_main()
        self.Menu_Butt = tk.Button(self.main_win, text="🏠", command=self.delete_PML_settings)
        self.Menu_Butt.place(x=0, y=0)
        self.scale = tk.Scale(self.main_win, from_=0, to=100, length=200, command=self.set_alpha, orient="horizontal", label="设置窗口透明度", bg=self.bg)
        self.scale.set(self.alpha * 100)
        self.scale.place(x=30, y=0)
        self.ColorSetLabel = tk.Label(self.main_win, text="设置背景颜色", bg=self.bg)
        self.ColorSetLabel.place(x=30, y=60)
        self.ColorChooser = tk.Button(self.main_win, text="点我设置背景颜色", command=self.set_color)
        self.ColorChooser.place(x=30, y=80)
    
    def AddNewUser(self):
        user_win = tk.Tk()
        user_win.title("添加用户")
        user_win.geometry("300x200")
        user_win.iconbitmap("./PML/ddd.ico")

        def check(event):
            if user_type.get() == "离线登录":
                label = tk.Label(user_win, text="用户名:")
                label.grid(column=1, row=2)
                self.Entry = tk.Entry(user_win)
                self.Entry.grid(column=2, row=2)

        def apply_func():
            if (self.Entry.get() != "" or not self.Entry.get().isspace()) and self.Entry.get().lower().isascii():
                self.username_listbox.insert(tk.END, self.Entry.get())
                self.UsernameList.append(self.Entry.get())
                user_win.destroy()
                self.save_all()
            elif not self.Entry.get().lower().isascii():
                messagebox.showerror("提示!", "用户名不可为中文!")
            else:
                messagebox.showerror("提示!", "笨蛋!你用户名都没填!")
        
        def cancel_func():
            user_win.destroy()

        label = tk.Label(user_win, text="用户名:")
        label.grid(column=1, row=2)
        self.Entry = tk.Entry(user_win)
        self.Entry.grid(column=2, row=2)
        tk.Label(user_win, text="用户类型:").grid(column=1, row=1)
        user_type = ttk.Combobox(user_win, values=["离线登录"], state="readonly")
        user_type.current(0)
        user_type.grid(column=2, row=1)
        user_type.bind('<<ComboboxSelected>>', check)
        cancel = ttk.Button(user_win, text="取消", command=cancel_func)
        cancel.grid(column=1, row=3)
        apply = ttk.Button(user_win, text="确认", command=apply_func)
        apply.grid(column=2, row=3)

        user_win.mainloop()
    
    def DeleteUser(self):
        if self.username_listbox.curselection() != ():
            self.UsernameList.remove(self.UsernameList[self.username_listbox.curselection()[0]])
            self.username_listbox.delete("active")
            self.save_all()
        else:
            tkinter.messagebox.showerror("错误!", "你没有选择用户!")

    def delete_settings(self):
        self.Menu_Butt.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.Add_User.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.Delete_User.destroy()
        self.main_win.update()
        time.sleep(0.06)
        self.UserDescription.destroy()
        self.username_listbox.destroy()
        self.main_win.update()
        self.create_main()
    
    def get_username_to_set(self, *args):
        if self.username_listbox.curselection() != ():
            self.current_username = self.username_listbox.get(self.username_listbox.curselection())
    
    def apply_username(self, *args):
        self.Username = self.current_username
        self.save_all()
        self.Start_Game_Label.config(text=f"是时候启动游戏了！\n正在使用的账户:{self.Username}\n准备启动游戏:{self.selected_version}")
        messagebox.showinfo("成功!", f"用户名已被设置为{self.Username}")

    def from_menu_to_user_settigs_page(self):
        self.delete_main()
        self.Menu_Butt = tk.Button(self.main_win, text="🏠", command=self.delete_settings)
        self.Menu_Butt.place(x=0, y=0)
        self.Add_User = tk.Button(self.main_win, text="➕", command=self.AddNewUser)
        self.Add_User.place(x=0, y=30)
        self.Delete_User = tk.Button(self.main_win, text="➖", command=self.DeleteUser)
        self.Delete_User.place(x=0, y=60)
        self.main_win.update()
        self.username_listbox = tk.Listbox(self.main_win, width=40, height=25)
        self.username_listbox.place(x=30, y=0)
        self.username_listbox.insert(tk.END, "正在加载...")
        self.main_win.update()
        self.username_listbox.delete(0)
        for i in self.UsernameList:
            if i != "" and not i.isspace():
                self.username_listbox.insert(tk.END, i)
        
        self.UserDescription = ttk.Frame(self.main_win, width=750, height=454, relief="ridge")
        self.UserDescription.place(x=350, y=0)
        self.UserDescriptionLabel = tk.Label(self.UserDescription, text="用户信息", font=("等线", 25))
        self.UserDescriptionLabel.place(x=20, y=0)
        self.username_listbox.bind("<<ListboxSelect>>", self.get_username_to_set)
        self.username_listbox.bind("<Double-Button-1>", self.apply_username)
    
    def check_support(self, *args):
        def main():
            if self.version_listbox.curselection() != ():
                self.download_version_to = self.version_listbox.get(self.version_listbox.curselection())
                self.SupportFabricLabel.config(text=f"Fabric支持:正在加载...")
                self.SupportForgeLabel.config(text=f"Forge支持:正在加载...")
                self.main_win.update()
                self.support_fabric = "true" if mll.fabric.is_minecraft_version_supported(self.version_listbox.get(self.version_listbox.curselection())) else "false"
                self.support_forge = "true" if mll.forge.find_forge_version(self.version_listbox.get(self.version_listbox.curselection())) is not None else "false"
                self.SupportFabricLabel.config(text=f"Fabric支持:{'支持' if self.support_fabric == 'true' else '不支持'}")
                self.SupportForgeLabel.config(text=f"Forge支持:{'支持' if self.support_forge == 'true' else '不支持'}")
                self.support_mod_loaders = ["原版"]
                self.ModLoaderVersion.set([])
                self.ModLoaderVersionOption.config(values=[])
                if self.support_fabric == "true":
                    self.support_mod_loaders.append("Fabric")
                if self.support_forge == "true":
                    self.support_mod_loaders.append("Forge")
                self.ModLoaderOption.config(values=self.support_mod_loaders)
                self.ModLoaderOption.current(0)
        
        t1 = threading.Thread(target=main)
        t1.start()
    
    def change_minecraft_dir(self):
        to_change = "/".join(os.path.abspath(tkinter.filedialog.askdirectory()).split("\\"))
        self.minecraft_dir = to_change
        if not os.path.exists(to_change + "/versions"):
            os.mkdir(to_change + "/versions")
        self.save_all()
        self.reload_versions()
    
    def reload_versions(self):
        self.downloaded_minecraft_versions = os.listdir(os.path.join(self.minecraft_dir, "versions"))
        self.VersionListListBox.delete(0, "end")
        for i in self.downloaded_minecraft_versions:
            if i != "" and not i.isspace():
                self.VersionListListBox.insert(0, i)

    def pre_do(self):
        tmp = []
        for i in self.ServerPath:
            tmp.append("".join("".join(i.split("\ "[:-1])).split("\'")))
        self.ServerPath = tmp

    def save_all(self):
        with open("./PML/PML.config", "w+") as f:
            self.pre_do()
            if self.bg is None:
                f.write(f"UsernameList = {self.UsernameList}\n" +
                        f"alpha = {self.alpha}\n" +
                        f"ServerList = {self.ServerList}\n" +
                        f'Background = ""\n' +
                        f'ServerPath = {self.ServerPath}\n' + 
                        f'LastDict = "{self.minecraft_dir}"\n' + 
                        f'LastLaunch = "{self.selected_version}"\n' + 
                        f'LastUsername = "{self.Username}"')
            elif self.ServerList == []:
                f.write(f"UsernameList = {self.UsernameList}\n" +
                        f"alpha = {self.alpha}\n" +
                        f"ServerList = []\n" +
                        f'Background = {self.bg}\n'  +
                        f'ServerPath = {self.ServerPath}\n' + 
                        f'LastDict = "{self.minecraft_dir}"\n' + 
                        f'LastLaunch = "{self.selected_version}"\n' + 
                        f'LastUsername = "{self.Username}"')
            else:
                f.write(f"UsernameList = {self.UsernameList}\n" +
                        f"alpha = {self.alpha}\n" +
                        f"ServerList = {self.ServerList}\n" +
                        f'Background = {self.bg}\n'  +
                        f'ServerPath = {self.ServerPath}\n' + 
                        f'LastDict = "{self.minecraft_dir}"\n' + 
                        f'LastLaunch = "{self.selected_version}"\n' + 
                        f'LastUsername = "{self.Username}"')

    def DeleteServer(self):
        if self.server_listbox.curselection() != ():
            self.ServerList.remove(self.server_listbox.curselection()[0])
            self.server_listbox.delete("active")
            
    def AddNewServer(self):
        self.Server_win = tk.Tk()
        self.Server_win.iconbitmap("./PML/ddd.ico")
        self.Server_win.geometry("400x300")
        self.Server_win.title("添加服务器")
        self.Server_win.resizable(False, False)

        def find_server_place():
            self.place = tkinter.filedialog.askopenfilename(title="服务器核心文件位置选择", filetypes=[("jar文件", "*.jar")])
            self.Server_Place.destroy()
            try:
                self.Label_Server_Place.config(text=self.place)
            except AttributeError:
                if len(self.place) <= 13:
                    self.Label_Server_Place = tk.Label(self.Server_win, text=self.place)
                else:
                    self.Label_Server_Place = tk.Label(self.Server_win, text=self.place[0:13] + "\n" + self.place[13:])
                self.Label_Server_Place.grid(row=2, column=2, columnspan=100)

            self.Server_Place = tk.Button(self.Server_win, text="更改", command=find_server_place)
            self.Server_Place.grid(row=3, column=1)
            self.jump_eula_loading.grid(column=1, row=4)
            self.create_server_button.grid(column=1, row=5, columnspan=100, padx=5)
        
        
        def create_server():
            try:            
                if self.place != "":
                    self.ServerList.append(self.Server_Name.get())
                    self.ServerPath.append(os.path.join("/".join(self.place.split(r'/')[:-1]), self.Server_Name.get(), os.path.basename(self.place)))
                    self.server_listbox.insert(tk.END, self.Server_Name.get())
                    tmp_working = os.getcwd()
                    os.chdir(os.path.abspath(os.path.dirname(self.place)))
                    os.mkdir(os.path.abspath(os.path.join(os.path.dirname(self.place), self.Server_Name.get())))
                    shutil.copyfile(os.path.abspath(self.place), os.path.abspath(os.path.join(os.path.dirname(self.place), self.Server_Name.get(), os.path.basename(self.place))))
                    os.chdir(os.path.join(os.path.abspath(os.path.dirname(self.place)), self.Server_Name.get()))
                    def run_server_once():
                        subprocess.call(["java", "-jar", f"./{os.path.basename(self.place)}"])
                        with open("./eula.txt", "w") as f:
                            f.write("eula=true")
                        os.chdir(tmp_working)
                        self.save_all()
                    
                    t1 = threading.Thread(target=run_server_once)
                    t1.start()
                else:
                    tkinter.messagebox.showerror("错误!", "你还没有选择服务器地址!")
            except AttributeError:
                tkinter.messagebox.showerror("错误!", "你还没有选择服务器地址!")


        tk.Label(self.Server_win, text="服务器名称:").grid(column=1, row=1)
        self.Server_Name = tk.Entry(self.Server_win)
        self.Server_Name.grid(column=2, row=1)
        tk.Label(self.Server_win, text="服务器位置:").grid(column=1, row=2)
        self.Server_Place = tk.Button(self.Server_win, text="选择服务器位置", command=find_server_place)
        self.Server_Place.grid(column=2, row=2)
        self.jump_eula_loading = tk.Checkbutton(self.Server_win, text="跳过EULA加载", onvalue="on", offvalue="off")
        self.jump_eula_loading.grid(column=1, row=3)
        self.jump_eula_loading.select()
        self.create_server_button = tk.Button(self.Server_win, text="创建服务器", width=54, relief="groove", command=create_server)
        self.create_server_button.grid(column=1, row=4, columnspan=100, padx=5)

        self.Server_win.mainloop()
    
    def set_status(self, status: str):
        self.status = status
        print(f"下载状态：{status}")

    def set_progress(self, progress: int):
        if self.current_max != 0:
            self.progress = f"{progress}/{self.current_max}"
            print(f"下载状态:{progress}/{self.current_max}")

    def set_max(self, new_max: int):
        self.current_max = new_max
    
    def download_version(self):
        if self.download_version_to != "":
            self.callback = {
            "setStatus": self.set_status,
            "setProgress": self.set_progress,
            "setMax": self.set_max
            }
            if self.ModLoader.get() == "原版":
                mll.install.install_minecraft_version(self.download_version_to, self.minecraft_dir, self.callback)
            elif self.ModLoader.get() == "Forge":
                mll.install.install_minecraft_version(self.download_version_to, self.minecraft_dir, callback=self.callback)
                mll.forge.install_forge_version(self.get_forge_versions(self.download_version_to)[0] if self.ModLoaderVersion.get().isspace() else self.ModLoaderVersion.get(),
                                                    self.minecraft_dir,
                                                    callback=self.callback)
            elif self.ModLoader.get() == "Fabric":
                mll.fabric.install_fabric(self.download_version_to, self.minecraft_dir, self.ModLoaderVersion.get(), self.callback)
            else:
                tkinter.messagebox.showerror("错误!", "你没有选择任何模组加载器!")

    def run_server(self):
        if self.server_listbox.curselection() != ():
            tmp_working = os.getcwd()
            os.chdir("/".join(self.ServerPath[self.server_listbox.curselection()[0]][2:-1].split("/")[:-1]))
            def runs():
                path = os.path.basename(self.ServerPath[self.server_listbox.curselection()[0]][1:-2])
                subprocess.call(["java", "-Xms1024M", "-Xmx4096M", "-jar", f"./{path}"])
                os.chdir(tmp_working)
            t2 = threading.Thread(target=runs)
            t2.start()
           
    def load_log(self):
        logpath = os.path.join(self.sever_path, "server.properties")
        self.ServerLog.delete(1.0, tk.END)
        try:
            with open(logpath) as f:
                self.ServerLog.insert(tk.END, f.read())
        except FileNotFoundError:
            self.ServerLog.insert(tk.END, "还没有服务器配置文件!")
            
    def delete_server_settings(self):
        self.Menu_Butt.destroy()
        self.Add_Server.destroy()
        self.Delete_Server.destroy()
        self.server_listbox.destroy()
        self.ServerDescription.destroy()
        self.ServerDescriptionLabel.destroy()
        self.create_main()
    
    def change_server(self, *args):
        if self.server_listbox.curselection() != ():
            self.sever_path = os.path.abspath("/".join(self.ServerPath[self.server_listbox.curselection()[0]][2:-2].split("/")[:-1]))
            self.ServerPath_Label.config(text=f"服务器核心位置:{self.ServerPath[self.server_listbox.curselection()[0]][2:-2]}")
            self.load_log()
    
    def save_prop(self, *args):
        logpath = os.path.join(self.sever_path, "server.properties")
        with open(logpath, "w") as f:
            f.write(self.ServerLog.get(1.0, tk.END))
        tkinter.messagebox.showinfo("成功", "已保存配置文件修改")
        self.load_log()

    def from_menu_to_server_page(self):
        self.delete_main()
        self.Menu_Butt = tk.Button(self.main_win, text="🏠", command=self.delete_server_settings)
        self.Menu_Butt.place(x=0, y=0)
        self.Add_Server = tk.Button(self.main_win, text="➕", command=self.AddNewServer)
        self.Add_Server.place(x=0, y=30)
        self.Delete_Server = tk.Button(self.main_win, text="➖", command=self.DeleteServer)
        self.Delete_Server.place(x=0, y=60)
        self.server_listbox = tk.Listbox(self.main_win, width=40, height=25)
        self.server_listbox.place(x=30, y=0)
        self.server_listbox.insert(tk.END, "正在加载...")
        self.server_listbox.bind("<<ListboxSelect>>", self.change_server)
        self.main_win.update()
        self.server_listbox.delete(0)
        for i in self.ServerList:
            if i != "" and not i.isspace():
                self.server_listbox.insert(tk.END, i)
        self.ServerDescription = ttk.Frame(self.main_win, width=750, height=454, relief="ridge")
        self.ServerDescription.place(x=350, y=0)
        self.ServerDescriptionLabel = tk.Label(self.ServerDescription, text="服务器面板", font=("等线", 25))
        self.ServerPath_Label = tk.Label(self.ServerDescription, text="服务器核心位置:")
        self.ServerPath_Label.place(x=20, y=60)
        self.ServerDescriptionLabel.place(x=20, y=0)
        self.StartServerButton = tk.Button(self.ServerDescription, text="启动这台服务器", command=self.run_server)
        self.StartServerButton.place(x=20, y=80)
        self.ServerLog = tk.Text(self.ServerDescription, width=80, height=23)
        self.ServerLog.place(x=130, y=80)
        self.ServerLog.bind("<Control-S>", self.save_prop)
        self.ServerLog.bind("<Control-s>", self.save_prop)
        self.Apply_Settings = tk.Button(self.ServerDescription, width=79, height=2, text="应用修改", command=self.save_prop)
        self.Apply_Settings.place(x=130, y=400)
    
    def get_forge_versions(self, version:str):
        all_forge_versions = mll.forge.list_forge_versions()
        output = []
        for i in all_forge_versions:
            version_split = i.split("-")
            if version_split[0] == version:
                output.append(version_split[1])
        return output
    
    def get_fabric_versions(self, version: str):
        all_fabric_versions = mll.fabric.get_all_loader_versions()
        output = []
        for i in all_fabric_versions:
            output.append(i["version"])
        return output     
    
    def load_mod_loader_version(self):
        if self.ModLoader.get() == "Forge":
            self.ModLoaderVersionOption.config(values=self.get_forge_versions(self.download_version_to))
        elif self.ModLoader.get() == "Fabric":
            self.ModLoaderVersionOption.config(values=self.get_fabric_versions(self.download_version_to))
        else:
            self.ModLoaderVersionOption.config(values=[])
    
    def get_mod_loader_version_theard(self, *args): threading.Thread(target=self.load_mod_loader_version).start()

    def from_menu_to_download_page(self):
        self.delete_main()
        self.Menu_Butt = tk.Button(self.main_win, text="🏠", command=self.delete_download)
        self.Menu_Butt.place(x=0, y=0)
        self.main_win.update()
        self.version_listbox = tk.Listbox(self.main_win, width=40, height=25)
        self.version_listbox.place(x=30, y=0)
        self.version_listbox.insert(tk.END, "正在加载...")
        self.VersionDescription = ttk.Frame(self.main_win, width=750, height=454, relief="ridge")
        self.VersionDescription.place(x=350, y=0)
        self.VersionDescriptionLabel = tk.Label(self.VersionDescription, text="版本概述", font=("等线", 25))
        self.VersionDescriptionLabel.place(x=20, y=0)
        self.SupportForgeLabel = tk.Label(self.VersionDescription, text="Forge支持:")
        self.SupportForgeLabel.place(x=20, y=60)
        self.SupportFabricLabel = tk.Label(self.VersionDescription, text="Fabric支持:")
        self.SupportFabricLabel.place(x=20, y=80)
        self.ModLoaderLabel = tk.Label(self.VersionDescription, text="选择模组加载器:")
        self.ModLoaderLabel.place(x=20, y=100)
        self.ModLoader = tk.StringVar()
        self.ModLoader.set("原版")
        self.ModLoaderOption = ttk.Combobox(self.VersionDescription, textvariable=self.ModLoader, values=["原版"], state="readonly")
        self.ModLoaderOption.place(x=150, y=100)
        self.ModLoaderOption.bind("<<ComboboxSelected>>", self.get_mod_loader_version_theard)
        self.ModLoaderVersionLabel = tk.Label(self.VersionDescription, text="选择Mod加载器版本:")
        self.ModLoaderVersionLabel.place(x=20, y=120)
        self.ModLoaderVersion = tk.StringVar()
        self.ModLoaderVersionOption = ttk.Combobox(self.VersionDescription, textvariable=self.ModLoaderVersion, values=[], state="readonly")
        self.ModLoaderVersionOption.place(x=150, y=120)
        self.DownloadButton = tk.Button(self.VersionDescription, text="下载Minecraft", width=30, height=1, command=self.download_minecraft_version_theard)
        self.DownloadButton.place(x=20, y=150)
        self.main_win.update()
        versionlist = self.get_version_list()
        self.version_listbox.delete(0)
        for i in versionlist:
            self.version_listbox.insert(tk.END, i["id"])
        self.version_listbox.bind("<<ListboxSelect>>", self.check_support)
        
        


MinecraftLauncher()
