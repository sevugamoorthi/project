from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


kv_code = """
WindowManager:
    IntroScreen:
    IntroImgScreen:
    MainScreen:
    NameScreen:
    DobScreen:
    FirstScreen:
    SecondScreen:


<IntroImgScreen>
    name: "Intro_img"
    FloatLayout:
        background_color: (39/255,150/255,126/255,1)
        background_normal: ""
        canvas.before:
            Color: 
                rgba: self.background_color
            Rectangle: 
                size: self.size 
                pos: self.pos
        orientation: 'vertical'
        Label:
            text: 'Baaloo G Iyer'
            font_size: 32
            pos_hint: {'center_x':0.5,'center_y':0.58}
        Image: 
            source: 'Baaloo.png'
            #size_hint: (None,None)
            pos_hint: {'center_x':0.5,'center_y':0.8}

        Label:
            text: 'As an expert in numerology, I possess a deep understanding of the profound influence numbers can have on various' 
            pos_hint: {'center_x':0.478,'center_y':0.5}

        Label:
            text: 'aspects of life. With a comprehensive knowledge of numerological principles, I adeptly interpret and analyze the'
            pos_hint: {'center_x':0.461,'center_y':0.45}

        Label:
            text: 'numbers, names, and dates, unraveling the hidden patterns and energies that shape individual destinies. My'
            pos_hint: {'center_x':0.448,'center_y':0.40}

        Label:
            text: 'expertise extends to providing insightful guidance on matters such as personal relationships, career paths, and life'
            pos_hint: {'center_x':0.470,'center_y':0.35}

        Label:
            text: 'decisions, empowering individuals to make informed choices based on the ancient wisdom embedded within the'
            pos_hint: {'center_x':0.463,'center_y':0.3}

        Label:
            text: 'numerical numerical fabric of their lives.'
            pos_hint: {'center_x':0.176,'center_y':0.25}
        Button:
            text: 'Get Started -->'
            background_color: (133/255,158/255,44/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            on_release: app.root.current = "main"
            pos_hint: {'center_x':0.5,'center_y':0.1}
            font_size: 25
            size_hint: None, None
            size: 250, 80

<MainScreen>:
    name: 'main'
    FloatLayout:
        background_color: (132/255,156/255,117/255,1)
        background_normal: ""
        canvas.before:
            Color: 
                rgba: self.background_color
            Rectangle: 
                size: self.size 
                pos: self.pos
        Label:
            text: "If you want to understand the behaviour of the name press 'Name' button"
            font_size: 24
            pos_hint: {'center_x':0.42,'center_y':0.9}
            
        Button:
            text: "Name"
            background_color: (52/255,128/255,102/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            font_size: 24
            size_hint: None, None
            size: 250, 80
            on_release: app.root.current = 'name_1'
            pos_hint: {'center_x':0.158,'center_y':0.78}

        Label:
            text: "If you want to understand the behaviour of the name press 'DOB' button"
            font_size: 24
            pos_hint: {'center_x':0.414,'center_y':0.6}
            
        Button:
            text: "DOB"
            background_color: (52/255,128/255,102/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            font_size: 24
            size_hint: None, None
            size: 250, 80
            on_release: app.root.current = 'dob_1'
            pos_hint: {'center_x':0.16,'center_y':0.48}

        Label:
            text: "If you want to understand the behaviour of the name press both 'Name & DOB' button"
            font_size: 24
            pos_hint: {'center_x':0.487,'center_y':0.3}
            
        Button:
            text: "Name & DOB"
            background_color: (52/255,128/255,102/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            font_size: 24
            size_hint: None, None
            size: 250, 80
            on_release: app.root.current = 'name'
            pos_hint: {'center_x':0.16,'center_y':0.18}

<NameScreen>:
    name: 'name_1'
    user_name: user_name
    fileName:fileName
    GridLayout:
        background_color: (161/255,127/255,40/255,1)
        background_normal: ""
        canvas.before:
            Color: 
                rgba: self.background_color
            Rectangle: 
                size: self.size 
                pos: self.pos
        spacing: 20
        padding: 40
        cols: 2
        Label:
            text: "Enter your name: "
            size_hint: None, None
            size: 450,120
            #pos_hint: {'center_x':0.5,'center_y':0.5}
            background_color: (49/255,35/255,176/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos

        TextInput: 
            id: user_name
            multiline: False
            size_hint: None, None
            size: 450,120

        Label:
            text: "Enter the path: "
            size_hint: None, None
            size: 450,120
            #pos_hint: {'center_x':0.5,'center_y':0.5}
            background_color: (49/255,35/255,176/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
        TextInput:
            id: fileName
            multiline: False
            size_hint: None, None
            size: 450,120

    FloatLayout:
        Button:
            text: "Save"
            background_color: (49/255,35/255,176/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            font_size: 30 
            size_hint: None,None
            size: 300,90
            pos_hint: {'center_x':0.3,'center_y':0.4}
            on_press: root.press()
            on_release: app.root.current = "second"

        Button:
            text: "Back"
            background_color: (49/255,35/255,176/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                RoundedRectangle: 
                    size: self.size 
                    pos: self.pos
                    radius: [30,30,30,30]
            font_size: 30 
            size_hint: None,None
            size: 300,90
            pos_hint: {'center_x':0.69,'center_y':0.4}
            on_release: app.root.current = "main"

<DobScreen>:
    name: 'dob_1'
    dob: dob 
    fileName: fileName
    background_color: (35/255,117/255,176/255,1)
    background_normal: ""
    canvas.before:
        Color: 
            rgba: self.background_color
        Rectangle: 
            size: self.size 
            pos: self.pos
    GridLayout:
        cols: 2
        spacing: 20
        padding: 40
        Label:
            text: "Enter your DOB: "
            size_hint: None, None
            size: 450,120
            #pos_hint: {'center_x':0.5,'center_y':0.5}
            background_color: (35/255,82/255,176/256,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos

        TextInput: 
            id: dob 
            multiline: False
            size_hint: None, None
            size: 450,120

        Label:
            text: "Enter the path: "
            size_hint: None, None
            size: 450,120
            #pos_hint: {'center_x':0.5,'center_y':0.5}
            background_color: (35/255,82/255,176/256,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
        TextInput:
            id: fileName
            multiline: False
            size_hint: None, None
            size: 450,120

    FloatLayout:
        Button:
            text: "Save"
            background_color: (35/255,82/255,176/256,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            font_size: 30 
            size_hint: None,None
            size: 300,90
            pos_hint: {'center_x':0.3,'center_y':0.4}
            on_press: root.press()
            on_release: app.root.current = "second"

        Button:
            text: "Back"
            background_color: (35/255,82/255,176/256,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                RoundedRectangle: 
                    size: self.size 
                    pos: self.pos
                    radius: [30,30,30,30]
            font_size: 30 
            size_hint: None,None
            size: 300,90
            pos_hint: {'center_x':0.69,'center_y':0.4}
            on_release: app.root.current = "main"

<FirstScreen>:
    #size: root.width, root.height
    background_color: (136/255,176/255,35/255,1)
    background_normal: ""
    canvas.before:
        Color: 
            rgba: self.background_color
        Rectangle: 
            size: self.size 
            pos: self.pos
    name: "name"
    user_name: user_name
    dob: dob
    fileName: fileName
    #GridLayout:
     #   spacing: 50
      #  padding:50
       # cols: 1
    GridLayout:
        cols: 2
        #size_hint: None,None
        #size: 500,500
        spacing: 18
        padding: 40
        Label:
            text: "Enter your name: "
            size_hint: None, None
            size: 450,120
            #pos_hint: {'center_x':0.5,'center_y':0.5}
            background_color: (35/255,176/255,61/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
        TextInput:
            id: user_name
            multiline: False
            size_hint: None, None
            size: 450,120
        Label:
            text: "Enter your DOB: "
            size_hint: None, None
            size: 450,120
            #pos_hint: {'center_x':0.5,'center_y':0.5}
            background_color: (35/255,176/255,61/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
        TextInput:
            id: dob
            multiline: False
            size_hint: None, None
            size: 450,120
        Label:
            text: "Enter the path: "
            size_hint: None, None
            size: 450,120
            #pos_hint: {'center_x':0.5,'center_y':0.5}
            background_color: (35/255,176/255,61/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
        TextInput:
            id: fileName
            multiline: False
            size_hint: None, None
            size: 450,120
            #row_force_default: True
            #row_default_height: 750

    FloatLayout:
        padding:0
        Button:
            text: "Save"
            background_color: (35/255,176/255,61/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            font_size: 30 
            size_hint: None,None
            size: 300,90
            pos_hint: {'center_x':0.3,'center_y':0.25}
            on_press: root.press()
            on_release: app.root.current = "second"

        Button:
            text: "Back"
            background_color: (35/255,176/255,61/255,1)
            background_normal: ""
            canvas.before:
                Color: 
                    rgba: self.background_color
                Rectangle: 
                    size: self.size 
                    pos: self.pos
            font_size: 30 
            size_hint: None,None
            size: 300,90
            pos_hint: {'center_x':0.69,'center_y':0.25}
            on_release: app.root.current = "main"


<SecondScreen>:
    name: "second"
    FloatLayout:
        padding: 30
        spacing: 17
        Label:
            text: "Your output file is saved in the desired directory!"
            font_size: 35
            #size_hint: (0.9,0.9)
            pos_hint: {'center_x':0.5,'center_y':0.7}
        Button:
            text: "Back"
            size_hint: (0.3,0.1)
            font_size: 23
            pos_hint: {'center_x':0.5,'center_y':0.5}
            on_release: app.root.current = "main"
"""

class FirstScreen(Screen):
    def press(self):
        user_name = self.user_name.text
        dob = self.dob.text
        fileName = self.fileName.text
    
        file = open("D:\\Numerology\\Name with DoB"+fileName,"w")
        
        a="1"
        b="2"
        c="3"
        d="4"
        e="5"
        f="8"
        g="3"
        h="5"
        i="1"
        j="1"
        k="2"
        l="3"
        m="4"
        n="5"
        o="7"
        p="8"
        q="5"
        r="2"
        s="3"
        t="4"
        u="6"
        v="6"
        w="6"
        x="5"
        y="1"
        z="5"
        
        print((" "*10)+"Your name is: "+user_name,file=file)
        #self.add_widget(Label(text=f"Name: {user_name}"))
        num = ""
        for i in user_name:
            i = i.lower()
            if i == "a":
                num += a
            elif i == "b":
                num += b
            elif i == "c":
                num += c
            elif i == "d":
                num += d 
            elif i == "e":
                num += e 
            elif i == "f":
                num += f 
            elif i == "g":
                num += g 
            elif i == "h": 
                num += h 
            elif i == "i":
                num += "1" 
            elif i == "j":
                num += j 
            elif i == "k":
                num += k 
            elif i == "l":
                num += l
            elif i == "m":
                num += m 
            elif i == "n":
                num += n 
            elif i == "o":
                num += o 
            elif i == "p":
                num += p 
            elif i == "q":
                num += q 
            elif i == "r":
                num += r 
            elif i == "s":
                num += s 
            elif i == "t":
                num += t 
            elif i == "u":
                num += u 
            elif i == "v":
                num += v 
            elif i == "w": 
                num += w 
            elif i == "x":
                num += x 
            elif i == "y":
                num += y 
            elif i == "z":
                num += z 
        print((" "*10)+"Number: "+num,file=file)
        #self.add_widget(Label(text=num))
        nums = num
        sum = 0
        newSum = ""
        sum1 = sum 
        count = 0
        hebrew = ""
        num1 = ""
        newSum1 = ""
        for i in range(len(num)-1):
            for j in num:
                try:
                    sum = int(num[count]) + int(num[count+1])
                except:
                    break
                if sum > 9:                                       
                    newSum += str(int(str(sum)[0]) + int(str(sum)[1]))    
                else:
                    newSum += str(sum) 
                count += 1 
            count = 0
            if int(newSum) < 10:
                break
            num = newSum
            newSum1 = newSum + " " + newSum1
            newSum = ""
        print("",file=file)
        #self.add_widget(Label(text=""))
        total = 0
        for i in nums:
            total += int(i)
        print((" "*10)+"Total:"+str(total),file=file) 
        print((" "*10)+"Hebrew: "+num,file=file)
        #self.add_widget(Label(text=str(total)))
        #self.add_widget(Label(text=num))
        newSum2 = newSum1.split(" ")
        for i in newSum2:
            print((" "*10)+i,file=file)
        #self.add_widget(Label(text=i))
        print("",file=file)

        #self.add_widget(Label(text=f"Your name is {name} and your DOB is {dob}"))

        #num = input()
        #print ("DOB: "+num)
        #self.add_widget(Label(text=f"Your DOB is: {dob}"))
        print((" "*10)+"Your DOB is: "+dob,file=file)
        num = self.dob.text
        nums = num
        sum = 0
        newSum = ""
        sum1 = sum 
        count = 0
        hebrew = ""
        num1 = ""
        newSum1 = ""
        for i in range(len(num)-1):
            for j in num:
                try:
                    sum = int(num[count]) + int(num[count+1])
                except:
                    break
                if sum > 9:                                       
                    newSum += str(int(str(sum)[0]) + int(str(sum)[1]))    
                else:
                    newSum += str(sum) 
                count += 1
            count = 0
            if int(newSum) < 10:
                break
            num = newSum
            newSum1 = newSum + " " + newSum1
            newSum = ""
        total = 0
        for i in nums:
            total += int(i)
        print((" "*10)+"Total: "+str(total),file=file)
        #self.add_widget(Label(text=f"Total: {total}")) 
        print((" "*10)+"Hebrew: "+num,file=file)
        #self.add_widget(Label(text=f"Hebrew: {num}"))
        print("",file=file)
        #self.add_widget(Label(text=f""))
        newSum2 = newSum1.split(" ")
        for i in newSum2:
            print((" "*10)+i,file=file)
            #self.add_widget(Label(text=i))
        self.user_name.text = ""
        self.dob.text = ""
        self.fileName.text = ""
        file.close()

class SecondScreen(Screen):
        pass

class IntroScreen(Screen):
    
    def __init__(self, **kwargs):
        super(IntroScreen, self).__init__(**kwargs)
        self.inn = Video(source='lv_0_20240114201246.mp4', state='play', options={'allow_stretch': True})

       # self.add_widget(self.intro_video)
        self.add_widget(self.inn)

    def on_touch_down(self, touch):
        # Skip the video on touch to proceed to the next screen
        App.get_running_app().root.current = 'Intro_img'

class IntroImgScreen(Screen):
        pass

class MainScreen(Screen):
        pass

class NameScreen(Screen):
    def press(self):
        user_name = self.user_name.text
        fileName = self.fileName.text
    
        file = open("D:\\Numerology\\Name"+fileName,"w")
        
        a="1"
        b="2"
        c="3"
        d="4"
        e="5"
        f="8"
        g="3"
        h="5"
        i="1"
        j="1"
        k="2"
        l="3"
        m="4"
        n="5"
        o="7"
        p="8"
        q="5"
        r="2"
        s="3"
        t="4"
        u="6"
        v="6"
        w="6"
        x="5"
        y="1"
        z="5"
        
        print((" "*10)+"Your name is: "+user_name,file=file)
        #self.add_widget(Label(text=f"Name: {user_name}"))
        num = ""
        for i in user_name:
            i = i.lower()
            if i == "a":
                num += a
            elif i == "b":
                num += b
            elif i == "c":
                num += c
            elif i == "d":
                num += d 
            elif i == "e":
                num += e 
            elif i == "f":
                num += f 
            elif i == "g":
                num += g 
            elif i == "h": 
                num += h 
            elif i == "i":
                num += "1" 
            elif i == "j":
                num += j 
            elif i == "k":
                num += k 
            elif i == "l":
                num += l
            elif i == "m":
                num += m 
            elif i == "n":
                num += n 
            elif i == "o":
                num += o 
            elif i == "p":
                num += p 
            elif i == "q":
                num += q 
            elif i == "r":
                num += r 
            elif i == "s":
                num += s 
            elif i == "t":
                num += t 
            elif i == "u":
                num += u 
            elif i == "v":
                num += v 
            elif i == "w": 
                num += w 
            elif i == "x":
                num += x 
            elif i == "y":
                num += y 
            elif i == "z":
                num += z 
        print((" "*10)+"Number: "+num,file=file)
        #self.add_widget(Label(text=num))
        nums = num
        sum = 0
        newSum = ""
        sum1 = sum 
        count = 0
        hebrew = ""
        num1 = ""
        newSum1 = ""
        for i in range(len(num)-1):
            for j in num:
                try:
                    sum = int(num[count]) + int(num[count+1])
                except:
                    break
                if sum > 9:                                       
                    newSum += str(int(str(sum)[0]) + int(str(sum)[1]))    
                else:
                    newSum += str(sum) 
                count += 1 
            count = 0
            if int(newSum) < 10:
                break
            num = newSum
            newSum1 = newSum + " " + newSum1
            newSum = ""
        print("",file=file)
        #self.add_widget(Label(text=""))
        total = 0
        for i in nums:
            total += int(i)
        print((" "*10)+"Total:"+str(total),file=file) 
        print((" "*10)+"Hebrew: "+num,file=file)
        #self.add_widget(Label(text=str(total)))
        #self.add_widget(Label(text=num))
        newSum2 = newSum1.split(" ")
        for i in newSum2:
            print((" "*10)+i,file=file)
        #self.add_widget(Label(text=i))
        print("",file=file)
        file.close()

        self.user_name.text = ""
        self.fileName.text = ""

class DobScreen(Screen):
    def press(self):
        dob = self.dob.text
        fileName = self.fileName.text
    
        file = open(fileName,"w")

        print((" "*10)+"Your DOB is: "+dob,file=file)
        num = self.dob.text
        nums = num
        sum = 0
        newSum = ""
        sum1 = sum 
        count = 0
        hebrew = ""
        num1 = ""
        newSum1 = ""
        for i in range(len(num)-1):
            for j in num:
                try:
                    sum = int(num[count]) + int(num[count+1])
                except:
                    break
                if sum > 9:                                       
                    newSum += str(int(str(sum)[0]) + int(str(sum)[1]))    
                else:
                    newSum += str(sum) 
                count += 1
            count = 0
            if int(newSum) < 10:
                break
            num = newSum
            newSum1 = newSum + " " + newSum1
            newSum = ""
        total = 0
        for i in nums:
            total += int(i)
        print((" "*10)+"Total: "+str(total),file=file)
        #self.add_widget(Label(text=f"Total: {total}")) 
        print((" "*10)+"Hebrew: "+num,file=file)
        #self.add_widget(Label(text=f"Hebrew: {num}"))
        print("",file=file)
        #self.add_widget(Label(text=f""))
        newSum2 = newSum1.split(" ")
        for i in newSum2:
            print((" "*10)+i,file=file)
            #self.add_widget(Label(text=i))
        self.dob.text = ""
        self.fileName.text = ""
        file.close()

class WindowManager(ScreenManager):
        pass

class BaalooApp(App):
    def build(self):
         self.icon = "Icon.ico"
         return Builder.load_string(kv_code)
    
if __name__ == "__main__":
    BaalooApp().run()