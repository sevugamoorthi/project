import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class MyGridLayout(GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)

        self.cols=2

        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="DOB: "))
        self.dob = TextInput(multiline=False)
        self.add_widget(self.dob)

        self.add_widget(Label(text=f"Enter the location: "))
        self.fileName = TextInput(multiline=False)
        self.add_widget(self.fileName)

        self.submit = Button(text="Submit",font_size=32)

        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self,instance):
        name = self.name.text
        dob = self.dob.text
        fileName = self.fileName.text

        file = open(fileName,"w")


        self.add_widget(Label(text=f"Your name is {name} and your DOB is {dob}"))

        #num = input()
        #print ("DOB: "+num)
        self.add_widget(Label(text=f"Your DOB is{dob}"))
        print("DOB is: "+dob,file=file)
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
        print("Total: "+str(total),file=file)
        self.add_widget(Label(text=f"Total: {total}")) 
        print("Hebrew: "+num,file=file)
        self.add_widget(Label(text=f"Hebrew is: {num}"))
        print("",file=file)
        self.add_widget(Label(text=f""))
        newSum2 = newSum1.split(" ")
        for i in newSum2:
            print(i,file=file)
            self.add_widget(Label(text=i))
        self.name.text = ""
        self.dob.text = ""
        file.close()

class BaalooApp(App):
    def build(self):
        clear_window = Widget()
        return MyGridLayout()
    
if __name__ == "__main__":
    BaalooApp().run()