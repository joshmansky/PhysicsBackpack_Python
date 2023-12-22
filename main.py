import kivymd
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
#from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.properties import ObjectProperty
from kivymd.uix.list import OneLineListItem
from kivy.uix.scrollview import ScrollView
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import math
from kivy.config import Config
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton


# Window.size = (292, 520)


def press(KV):
    name = ("Acceleration is " + KV.ids.velocity.text / KV.ids.time.text + "m/s^2")

    KV.ids.accel.text = name


KV = """
<ContentNavigationDrawer>:
    orientation: 'vertical'
    padding: "5dp"
    spacing: "5dp"

    AnchorLayout:
        anchor_x: "right"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: (1,1)
            source: "Screen Shot 2021-07-11 at 8.34.30 PM.png"

    ScrollView:

        MDList:

            MDLabel:
                text: 'Calculators'
                font_style: 'Subtitle1'
                size_hint_y: None
                height:self.texture_size[1]
                spacing: '5dp' 


            OneLineIconListItem:
                text: 'Newtonian Mechanics'

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "motion_screen"

                IconLeftWidget:
                    icon: 'apple'


            OneLineIconListItem:
                text: 'Electromagnetism'

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "elec_screen"

                IconLeftWidget:
                    icon: 'lightning-bolt'


            OneLineIconListItem:
                text: 'Fluid Mechanics'

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "thermo_screen"

                IconLeftWidget:
                    icon: 'home-thermometer'


            OneLineIconListItem:
                text: 'Atomic Physics'

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "atomic_screen"

                IconLeftWidget:
                    icon: 'atom'


            MDLabel:
                text: 'Other'
                font_style: 'Subtitle1'
                size_hint_y: None
                height:self.texture_size[1]                                


            OneLineIconListItem:
                text: 'Other Resources'

                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "resource_screen"

                IconLeftWidget:
                    icon: 'file-table' 

<AccelerationScreen>:
    name: "acceleration_screen"

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y": 0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: time
        input_filter: 'float'
        hint_text: 'Enter Time'
        helper_text: "In seconds"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y": 0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: accel
        input_filter: 'float'
        hint_text: 'Acceleration'
        helper_text: "In m/s^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y": 0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon: "calculator"
        text: 'Calculate Velocity'
        pos_hint: {'center_x': 0.5, "center_y": 0.50}
        on_release:
            # print("Click")
            app.accelvelocity()

    MDFillRoundFlatIconButton:
        icon: "calculator"
        text: 'Calculate Time'
        pos_hint: {'center_x': 0.5, "center_y": 0.40}
        on_release:
            # print("Click")
            app.acceltime()

    MDFillRoundFlatIconButton:
        icon: "calculator"
        text: 'Calculate Acceleration'
        pos_hint: {'center_x': 0.5, "center_y": 0.30}
        on_release:
            # print("Click")
            app.acceleration()

    Image:
        size_hint: (None, None)
        size: ("100dp", "100dp")
        source: "acceleration-equation.png"
        pos_hint: {'center_x': 0.5, "center_y": 0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y": 0.05}
        on_release:
            # print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"


<DisplacementScreen>:
    name: "displacement_screen"

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: time
        input_filter: 'float'
        hint_text: 'Enter Time'
        helper_text: "In seconds"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: displacement
        input_filter: 'float'
        hint_text: 'Enter Displacement'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.disvelocity()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Time'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.distime()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Displacement'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.displacement()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-22 at 11.00.48 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"


<DensityScreen>:
    name: "density_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: volume
        input_filter: 'float'
        hint_text: 'Enter Volume'
        helper_text: "In m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: density
        input_filter: 'float'
        hint_text: 'Enter Density'
        helper_text: "In kg/m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.denmass()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Volume'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.denvolume()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Density'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.density()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "density1EQ.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"


<PhaseVelocityScreen>:
    name: "phase_velocity_screen"

    MDTextField:
        id: wavelength
        input_filter: 'float'
        hint_text: 'Enter Wavelength'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: period
        input_filter: 'float'
        hint_text: 'Enter Period'
        helper_text: "In s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: phase_velocity
        input_filter: 'float'
        hint_text: 'Enter Phase Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Wavelength'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.phasewave()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Period'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.phaseperiod()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Phase Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.phasevelocity()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 7.55.31 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"

<WavelengthScreen>:
    name: "wavelength_screen"

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: frequency
        input_filter: 'float'
        hint_text: 'Enter Frequency'
        helper_text: "In Hz"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: wavelength
        input_filter: 'float'
        hint_text: 'Enter Wavelength'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.wavvelocity()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Frequency'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.wavfrequency()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Wavelength'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.wavelength()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 7.02.48 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "atomic_screen"
            root.screen_manager.transition.direction = "right"   


<StaticFluidPressureScreen>:
    name: "static_fluid_pressure_screen"

    MDTextField:
        id: density
        input_filter: 'float'
        hint_text: 'Enter Density'
        helper_text: "In kg/m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: gravitational_acceleration
        input_filter: 'float'
        hint_text: 'Enter Gravitational Acceleration'
        helper_text: "In m/s^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: depth
        input_filter: 'float'
        hint_text: 'Enter Depth'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: pressure
        input_filter: 'float'
        hint_text: 'Enter Pressure'
        helper_text: "In kg/m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.65}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Density'
        pos_hint: {'center_x': 0.5, "center_y":0.55}
        on_release: 
            #print("Click")
            app.staticdensity()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Gravitational Acceleration'
        pos_hint: {'center_x': 0.5, "center_y":0.46}
        on_release: 
            #print("Click")
            app.staticgravity()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Wavelength'
        pos_hint: {'center_x': 0.5, "center_y":0.37}
        on_release: 
            #print("Click")
            app.staticdepth()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Wavelength'
        pos_hint: {'center_x': 0.5, "center_y":0.28}
        on_release: 
            #print("Click")
            app.staticpressure()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 9.38.30 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"   


<DynamicPressureScreen>:
    name: "dynamic_pressure_screen"

    MDTextField:
        id: density
        input_filter: 'float'
        hint_text: 'Enter Density'
        helper_text: "In kg/m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: flow_speed
        input_filter: 'float'
        hint_text: 'Enter Flow Speed'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: pressure
        input_filter: 'float'
        hint_text: 'Enter Gravitational Acceleration'
        helper_text: "In Pa"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Density'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.wavvelocity()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Flow Speed'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.wavfrequency()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Pressure'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.wavelength()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 9.44.08 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"   


<BuoyancyScreen>:
    name: "buoyancy_screen"

    MDTextField:
        id: density
        input_filter: 'float'
        hint_text: 'Enter Density'
        helper_text: "In kg/m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: displaced_volume
        input_filter: 'float'
        hint_text: 'Enter Displaced Volume'
        helper_text: "In m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: gravitational_acceleration
        input_filter: 'float'
        hint_text: 'Enter Gravitational Acceleration'
        helper_text: "In m/s^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: buoyancy
        input_filter: 'float'
        hint_text: 'Enter Buoyancy'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Density'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.buoyancyden()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Gravitational Acceleration'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.buoyancydis()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Wavelength'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.buoyancygra()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Buoyancy'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.buoyancy()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 10.06.17 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"   


<VolumetricFlowRateScreen>:
    name: "volumetric_flow_rate_screen"

    MDTextField:
        id: flow_velocity
        input_filter: 'float'
        hint_text: 'Enter Flow Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: cross_sectional_vector_area
        input_filter: 'float'
        hint_text: 'Enter Cross-Sectional Vector Area'
        helper_text: "In m^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: volumetric_flow_rate
        input_filter: 'float'
        hint_text: 'Enter Volumetric Flow Rate'
        helper_text: "In m/s^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Flow Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.volumetricflo()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Cross-Sectional Vector Area'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.volumetriccro()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Volumetric Flow Rate'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.volumetric()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 10.24.12 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"   


<MassFlowRateScreen>:
    name: "mass_flow_rate_screen"

    MDTextField:
        id: change_in_mass
        input_filter: 'float'
        hint_text: 'Enter Change in Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: change_in_time
        input_filter: 'float'
        hint_text: 'Enter Change in Time'
        helper_text: "In s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: mass_flow_rate
        input_filter: 'float'
        hint_text: 'Enter Mass Flow Rate'
        helper_text: "In kg/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Flow Change in Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.masschm()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Change in Time'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.masscht()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass Flow Rate'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.mass()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 10.41.14 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"   


<HeatCapacityScreen>:
    name: "heat_capacity_screen"

    MDTextField:
        id: energy
        input_filter: 'float'
        hint_text: 'Enter Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: difference_in_temperature
        input_filter: 'float'
        hint_text: 'Enter Difference in Temperature'
        helper_text: "In K"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: heat_capacity
        input_filter: 'float'
        hint_text: 'Enter Heat Capacity'
        helper_text: "In J/K"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.heatene()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Difference in Temperature'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.heatdif()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Heat Capacity'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.heat()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 10.52.10 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"  


<DeBroglieWavelengthScreen>:
    name: "de_broglie_wavelength_screen"

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: wavelength
        input_filter: 'float'
        hint_text: 'Enter Heat Capacity'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.devel()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.demas()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Wavelength'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.dewav()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 11.07.42 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "atomic_screen"
            root.screen_manager.transition.direction = "right"  


<MechanicalAdvantageScreen>:
    name: "mechanical_advantage_screen"

    MDTextField:
        id: output_force
        input_filter: 'float'
        hint_text: 'Enter Output Force'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: input_force
        input_filter: 'float'
        hint_text: 'Enter Input Force'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: mechanical_advantage
        input_filter: 'float'
        hint_text: 'Enter Mechanical Advantage'
        helper_text: " "
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Output Force'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.mechanicalout()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Input Force'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.mechanicalinp()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mechanical Advantage'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.mechanical()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 11.39.13 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"  


<IndexOfRefractionScreen>:
    name: "index_of_refraction_screen"

    MDTextField:
        id: speed_of_light_in_medium
        input_filter: 'float'
        hint_text: 'Enter Speed of Light in Medium'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: index_of_refraction
        input_filter: 'float'
        hint_text: 'Enter Index of Refraction'
        helper_text: " "
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Speed of Light in Medium'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.indexspe()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Index of Refraction'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.index()      

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-16 at 11.58.33 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "thermo_screen"
            root.screen_manager.transition.direction = "right"  


<NewtonsSecondLawScreen>:
    name: "newton's_second_law_screen"

    MDTextField:
        id: acceleration
        input_filter: 'float'
        hint_text: 'Enter Acceleration'
        helper_text: "In m/s^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Acceleration'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.newtonacc()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.newtonmas()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.newtonfor()  

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-22 at 10.52.12 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right"  


<GravitationalAccelerationScreen>:
    name: "gravitational_acceleration_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: gravitational_acceleration
        input_filter: 'float'
        hint_text: 'Enter Gravitational Acceleration'
        helper_text: "In m/s^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.gravitationalmas()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.gravitationalfor()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Gravitational Acceleration'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.gravitational()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 2.25.58 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right"  


<NewtonsLawOfUniversalGravitationScreen>:
    name: "newton's_law_of_universal_gravitation_screen"

    MDTextField:
        id: mass_1
        input_filter: 'float'
        hint_text: 'Enter Mass 1'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: mass_2
        input_filter: 'float'
        hint_text: 'Enter Mass 2'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: distance_between_two_masses
        input_filter: 'float'
        hint_text: 'Enter Distance Between Two Masses'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force of Gravity'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass 1'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.universalm1()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass 2'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.universalm2()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Distance Between Two Masses'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.universaldis()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force of Gravity'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.universalfor()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 2.51.59 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right"   


<HookesLawScreen>:
    name: "hooke's_law_screen"

    MDTextField:
        id: spring_constant
        input_filter: 'float'
        hint_text: 'Enter Spring Constant'
        helper_text: "In N/m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: deformation
        input_filter: 'float'
        hint_text: 'Enter Deformation'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Spring Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Spring Constant'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.hookesspr()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Deformation'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.hookesdef()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Spring Force'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.hookesfor()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 3.21.13 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right"  


<MomentumScreen>:
    name: "momentum_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: momentum
        input_filter: 'float'
        hint_text: 'Enter Momentum'
        helper_text: "In kg*m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.momentummas()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.momentumvel()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Momentum'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.momentum()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 3.36.44 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<WorkScreen>:
    name: "work_screen"

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: displacement
        input_filter: 'float'
        hint_text: 'Enter Displacement'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: work
        input_filter: 'float'
        hint_text: 'Enter Work'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.workfor()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Displacement'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.workdis()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Work'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.work()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-22 at 10.00.40 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<KineticEnergyScreen>:
    name: "kinetic_energy_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: kinetic_energy
        input_filter: 'float'
        hint_text: 'Enter Kinetic Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.kineticmas()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.kineticvel()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Kinetic Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.kinetic()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 3.51.48 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<PotentialEnergyScreen>:
    name: "potential_energy_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: gravitational_acceleration
        input_filter: 'float'
        hint_text: 'Enter Gravitational Acceleration'
        helper_text: "In m/s^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: height
        input_filter: 'float'
        hint_text: 'Enter Height'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: potential_energy
        input_filter: 'float'
        hint_text: 'Enter Potential Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.potentialmas()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Gravitational Acceleration'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.potentialgra()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Height'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.potentialhei()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Potential Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.potential()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 4.02.33 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right"   


<ElasticEnergyScreen>:
    name: "elastic_energy_screen"

    MDTextField:
        id: spring_constant
        input_filter: 'float'
        hint_text: 'Enter Spring Constant'
        helper_text: "In N/m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: deformation
        input_filter: 'float'
        hint_text: 'Enter deformation'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: elastic_energy
        input_filter: 'float'
        hint_text: 'Enter Elastic Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Spring Constant'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.elasticspr()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Deformation'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.elasticdef()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Elastic Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.elastic()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 4.14.31 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<EnergyConversionEfficiencyScreen>:
    name: "energy_conversion_efficiency_screen"

    MDTextField:
        id: output_power
        input_filter: 'float'
        hint_text: 'Enter Output Power'
        helper_text: "In W"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: input_power
        input_filter: 'float'
        hint_text: 'Enter Input Power'
        helper_text: "In W"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: efficiency
        input_filter: 'float'
        hint_text: 'Enter Efficiency'
        helper_text: "In Percentage"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Output Power'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.energyout()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Input Power'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.energyin()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Efficiency'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.energyeff()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 4.30.00 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<PressureScreen>:
    name: "pressure_screen"

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: area
        input_filter: 'float'
        hint_text: 'Enter Area'
        helper_text: "In m^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: pressure
        input_filter: 'float'
        hint_text: 'Enter Pressure'
        helper_text: "In Pa"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.pressurefor()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Area'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.pressureare()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Pressure'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.pressure()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 4.41.45 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<PressureVolumeWorkScreen>:
    name: "pressure_volume_work_screen"

    MDTextField:
        id: pressure
        input_filter: 'float'
        hint_text: 'Enter Pressure'
        helper_text: "In Pa"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: volume
        input_filter: 'float'
        hint_text: 'Enter Volume'
        helper_text: "In m^3"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: pv_work
        input_filter: 'float'
        hint_text: 'Enter PV Work'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Pressure'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.pvpressure()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Volume'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.pvvolume()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate PV Work'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.pvwork()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 4.50.53 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<CentrifugalForceScreen>:
    name: "centrifugal_force_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: radius
        input_filter: 'float'
        hint_text: 'Enter Radius'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Centrifugal Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.centrifugalmas()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.centrifugalvel()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Radius'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.centrifugalrad()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Centrifugal Force'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.centrifugal()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 4.59.34 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right"   


<CoulombsLawScreen>:
    name: "coulomb's_law_screen"

    MDTextField:
        id: charge_1
        input_filter: 'float'
        hint_text: 'Enter Charge 1'
        helper_text: "In C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: charge_2
        input_filter: 'float'
        hint_text: 'Enter Charge 2'
        helper_text: "In C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: distance
        input_filter: 'float'
        hint_text: 'Enter Distance'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Charge 1'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.coulombc1()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Charge 2'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.coulombc2()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Distance'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.coulombdis()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.coulombfor()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 5.15.07 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"   


<FrictionScreen>:
    name: "friction_screen"

    MDTextField:
        id: friction_coefficient
        input_filter: 'float'
        hint_text: 'Enter Friction Coefficient'
        helper_text: " "
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: normal_force
        input_filter: 'float'
        hint_text: 'Enter Normal Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: friction
        input_filter: 'float'
        hint_text: 'Enter Friction'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Friction Coefficient'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.frictioncoe()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Normal Force'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.frictionnor()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Friction'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.friction()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 5.31.23 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<TorqueScreen>:
    name: "torque_screen"

    MDTextField:
        id: radius
        input_filter: 'float'
        hint_text: 'Enter radius'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: angle
        input_filter: 'float'
        hint_text: 'Enter Angle Between Force and Lever'
        helper_text: "In degrees"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: torque
        input_filter: 'float'
        hint_text: 'Enter Torque'
        helper_text: "kg⋅m^2⋅s^−2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Radius'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.torquerad()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.torquefor()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Angle Between Force and Lever'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.torqueang()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Torque'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.torque()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 5.39.50 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right"   


<RotationalKineticEnergyScreen>:
    name: "rotational_kinetic_energy_screen"

    MDTextField:
        id: angular_velocity
        input_filter: 'float'
        hint_text: 'Enter Angular Velocity'
        helper_text: "Hz"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: moment_of_inertia
        input_filter: 'float'
        hint_text: 'Enter Moment of Inertia'
        helper_text: "In kg⋅m^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: rotational_kinetic_energy
        input_filter: 'float'
        hint_text: 'Enter Rotational Kinetic Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Angular Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.rotationalang()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Moment of Inertia'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.rotationalmom()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Rotational Kinetic Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.rotational()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 5.59.05 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "motion_screen"
            root.screen_manager.transition.direction = "right" 


<ElectricPowerScreen>:
    name: "electric_power_screen"

    MDTextField:
        id: voltage
        input_filter: 'float'
        hint_text: 'Enter Voltage'
        helper_text: "V"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: current
        input_filter: 'float'
        hint_text: 'Enter Current'
        helper_text: "In A"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: power
        input_filter: 'float'
        hint_text: 'Enter Power'
        helper_text: "In W"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Voltage'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.powervol()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Current'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.powercur()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Power'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.power()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 7.32.42 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right" 


<ElectricCurrentScreen>:
    name: "electric_current_screen"

    MDTextField:
        id: charge
        input_filter: 'float'
        hint_text: 'Enter Charge'
        helper_text: "In C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: time
        input_filter: 'float'
        hint_text: 'Enter Time'
        helper_text: "In s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: current
        input_filter: 'float'
        hint_text: 'Enter Current'
        helper_text: "In A"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Charge'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.currentcha()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Current'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.currenttim()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Power'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.current()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "ElecCurrent.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right" 


<OhmsLawScreen>:
    name: "ohm's_law_screen"

    MDTextField:
        id: current
        input_filter: 'float'
        hint_text: 'Enter Current'
        helper_text: "In A"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: resistance
        input_filter: 'float'
        hint_text: 'Enter Resistance'
        helper_text: "In Ohm's"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: voltage
        input_filter: 'float'
        hint_text: 'Enter Voltage'
        helper_text: "In V"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Current'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.ohmscurrent()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Resistance'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.ohmsresistance()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Voltage'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.ohmsvoltage()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 7.51.11 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"


<VoltageScreen>:
    name: "voltage_screen"

    MDTextField:
        id: energy
        input_filter: 'float'
        hint_text: 'Enter Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: charge
        input_filter: 'float'
        hint_text: 'Enter Charge'
        helper_text: "In C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: voltage
        input_filter: 'float'
        hint_text: 'Enter Voltage'
        helper_text: "In V"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.voltageene()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Charge'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.voltagecha()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Voltage'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.voltage()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 8.05.08 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"

<ResistivityScreen>:
    name: "resistivity_screen"

    MDTextField:
        id: length
        input_filter: 'float'
        hint_text: 'Enter Length'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: area
        input_filter: 'float'
        hint_text: 'Enter Area'
        helper_text: "In m^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: resistance
        input_filter: 'float'
        hint_text: 'Enter Resistance'
        helper_text: "In Ohm's"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: resistivity
        input_filter: 'float'
        hint_text: 'Enter Resistivity'
        helper_text: "In Ohm's * m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Length'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.resistivitylen()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Area'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.resistivityare()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Resistance'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.resistivityres()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Resistivity'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.resistivity()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 8.15.34 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"   


<CapacitanceScreen>:
    name: "capacitance_screen"

    MDTextField:
        id: charge
        input_filter: 'float'
        hint_text: 'Enter Charge'
        helper_text: "In C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: voltage
        input_filter: 'float'
        hint_text: 'Enter Voltage'
        helper_text: "In V"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: capacitance
        input_filter: 'float'
        hint_text: 'Enter Capacitance'
        helper_text: "In F"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Charge'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.capacitancecha()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Voltage'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.capacitancevol()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Capacitance'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.capacitance()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 8.37.23 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"


<CapacitorEnergyScreen>:
    name: "capacitor_energy_screen"

    MDTextField:
        id: energy
        input_filter: 'float'
        hint_text: 'Enter Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: voltage
        input_filter: 'float'
        hint_text: 'Enter Voltage'
        helper_text: "In V"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: capacitance
        input_filter: 'float'
        hint_text: 'Enter Capacitance'
        helper_text: "In F"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.capacitorene()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Voltage'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.capacitorvol()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Capacitance'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.capacitorcap()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 8.45.19 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"


<InductorEnergyScreen>:
    name: "inductor_energy_screen"

    MDTextField:
        id: inductance
        input_filter: 'float'
        hint_text: 'Enter Inductance'
        helper_text: "In H"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: current
        input_filter: 'float'
        hint_text: 'Enter Current'
        helper_text: "In A"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: energy
        input_filter: 'float'
        hint_text: 'Enter Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Inductance'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.inductorind()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Current'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.inductorcur()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.inductorene()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 8.52.33 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"


<EnergyScreen>:
    name: "energy_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: momentum
        input_filter: 'float'
        hint_text: 'Enter Momentum'
        helper_text: "In kg*m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: energy
        input_filter: 'float'
        hint_text: 'Enter Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.energymas()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Momentum'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.energymom()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.energy()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 9.11.21 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "atomic_screen"
            root.screen_manager.transition.direction = "right"


<KEMaxScreen>:
    name: "ke_max_screen"

    MDTextField:
        id: frequency
        input_filter: 'float'
        hint_text: 'Enter Frequency'
        helper_text: "In Hz"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: work_function
        input_filter: 'float'
        hint_text: 'Enter Work Function'
        helper_text: "In eV"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.6}
        size_hint: None, None
        width: 290

    MDTextField:
        id: energy
        input_filter: 'float'
        hint_text: 'Enter Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Frequency'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.kefre()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Work Function'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.kewor()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.keene()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 9.14.17 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "atomic_screen"
            root.screen_manager.transition.direction = "right"

<MassEnergyEquivalenceScreen>:
    name: "mass_energy_equivalence_screen"

    MDTextField:
        id: mass
        input_filter: 'float'
        hint_text: 'Enter Mass'
        helper_text: "In kg"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.75}
        size_hint: None, None
        width: 290

    MDTextField:
        id: energy
        input_filter: 'float'
        hint_text: 'Enter Energy'
        helper_text: "In J"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Mass'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.massmas()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Energy'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.massene()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-17 at 9.19.18 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "atomic_screen"
            root.screen_manager.transition.direction = "right"


<MagneticFieldScreen>:
    name: "magnetic_field_screen"

    MDTextField:
        id: current
        input_filter: 'float'
        hint_text: 'Enter Current'
        helper_text: "In A"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.70}
        size_hint: None, None
        width: 290

    MDTextField:
        id: distance_from_wire
        input_filter: 'float'
        hint_text: 'Enter The Distance From the Wire'
        helper_text: "In m"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.80}
        size_hint: None, None
        width: 290

    MDTextField:
        id: magnetic_field
        input_filter: 'float'
        hint_text: 'Enter Magnetic Field'
        helper_text: "In T"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Current'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.magneticcur()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Distance From Wire'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.magneticdis()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Magnetic Field'
        pos_hint: {'center_x': 0.5, "center_y":0.60}
        on_release: 
            #print("Click")
            app.magneticfie()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-18 at 3.00.54 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"


<ElectricFieldScreen>:
    name: "electric_field_screen"

    MDTextField:
        id: force
        input_filter: 'float'
        hint_text: 'Enter Force'
        helper_text: "In N"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.70}
        size_hint: None, None
        width: 290

    MDTextField:
        id: charge
        input_filter: 'float'
        hint_text: 'Enter Charge'
        helper_text: "In C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.80}
        size_hint: None, None
        width: 290

    MDTextField:
        id: electric_field
        input_filter: 'float'
        hint_text: 'Enter Electric Field'
        helper_text: "In N/C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.90}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Force'
        pos_hint: {'center_x': 0.5, "center_y":0.40}
        on_release: 
            #print("Click")
            app.electricfor()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Charge'
        pos_hint: {'center_x': 0.5, "center_y":0.60}
        on_release: 
            #print("Click")
            app.electriccha()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Electric Field'
        pos_hint: {'center_x': 0.5, "center_y":0.50}
        on_release: 
            #print("Click")
            app.electricfie()

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-18 at 2.51.15 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.18}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"


<MagneticFluxScreen>:
    name: "magnetic_flux_screen"

    MDTextField:
        id: angle
        input_filter: 'float'
        hint_text: 'Enter Angle'
        helper_text: "In Degrees"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: area
        input_filter: 'float'
        hint_text: 'Enter Area'
        helper_text: "In m^2"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.85}
        size_hint: None, None
        width: 290

    MDTextField:
        id: magnetic_field
        input_filter: 'float'
        hint_text: 'Enter Magnetic Field'
        helper_text: "In T"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.76}
        size_hint: None, None
        width: 290

    MDTextField:
        id: magnetic_flux
        input_filter: 'float'
        hint_text: 'Enter Magnetic Flux'
        helper_text: "In Wb"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.67}
        size_hint: None, None
        width: 290

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Angle'
        pos_hint: {'center_x': 0.5, "center_y":0.57}
        on_release: 
            #print("Click")
            app.fluxang()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Area'
        pos_hint: {'center_x': 0.5, "center_y":0.48}
        on_release: 
            #print("Click")
            app.fluxare()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Magnetic Field'
        pos_hint: {'center_x': 0.5, "center_y":0.39}
        on_release: 
            #print("Click")
            app.fluxmag()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Magnetic Flux'
        pos_hint: {'center_x': 0.5, "center_y":0.30}
        on_release: 
            #print("Click")
            app.flux()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-18 at 3.40.41 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.16}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.05}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"   


<MagneticForceScreen>:
    name: "magnetic_force_screen"

    MDTextField:
        id: charge
        input_filter: 'float'
        hint_text: 'Enter Charge of Moving Particle'
        helper_text: "In C"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.94}
        size_hint: None, None
        width: 290

    MDTextField:
        id: magnetic_field
        input_filter: 'float'
        hint_text: 'Enter Magnetic Field'
        helper_text: "In T"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.86}
        size_hint: None, None
        width: 290

    MDTextField:
        id: angle
        input_filter: 'float'
        hint_text: 'Enter Angle'
        helper_text: "In Degrees"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.77}
        size_hint: None, None
        width: 290

    MDTextField:
        id: velocity
        input_filter: 'float'
        hint_text: 'Enter Particle Velocity'
        helper_text: "In m/s"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.68}
        size_hint: None, None
        width: 290

    MDTextField:
        id: magnetic_force
        input_filter: 'float'
        hint_text: 'Enter Magnetic Force'
        helper_text: "In H"
        helper_text_mode: "on_focus"
        icon_right_color: app.theme_cls.primary_color
        icon_right: 'equal-box'
        pos_hint: {'center_x': 0.5, "center_y":0.59}
        size_hint: None, None
        width: 290


    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Particle Velocity'
        pos_hint: {'center_x': 0.5, "center_y":0.51}
        on_release: 
            #print("Click")
            app.forcevel()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Charge of Moving Particle'
        pos_hint: {'center_x': 0.5, "center_y":0.43}
        on_release: 
            #print("Click")
            app.forcecha()

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Angle'
        pos_hint: {'center_x': 0.5, "center_y":0.35}
        on_release: 
            #print("Click")
            app.forceang()      

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Magnetic Field'
        pos_hint: {'center_x': 0.5, "center_y":0.27}
        on_release: 
            #print("Click")
            app.forcefie()  

    MDFillRoundFlatIconButton:
        icon:  "calculator"
        text: 'Calculate Magnetic Force'
        pos_hint: {'center_x': 0.5, "center_y":0.19}
        on_release: 
            #print("Click")
            app.force()             

    Image:
        size_hint: (None,None)
        size: ("100dp", "100dp")
        source: "Screen Shot 2021-07-22 at 10.49.44 PM.png"
        pos_hint: {'center_x': 0.5, "center_y":0.12}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, "center_y":0.04}
        on_release: 
            #print("Click?")
            root.screen_manager.current = "elec_screen"
            root.screen_manager.transition.direction = "right"   


<ConstantsScreen>:
    name: "constants_screen"  

    BoxLayout:
        id:constants_table

    BoxLayout: 
        orientation: "vertical" 
        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 

<UnitsScreen>:
    name: "units_screen"  

    BoxLayout:
        id:units_table                

    BoxLayout: 
        orientation: "vertical" 
        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<AlphabetScreen>:
    name: "alphabet_screen"  

    BoxLayout:
        id:alphabet_table

    BoxLayout: 
        orientation: "vertical"        
        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right"                        


<ElectronOrbitalsScreen>:
    name: "electron_orbitals_screen"  

    BoxLayout: 
        orientation: "vertical"     
        Image:
            source: "ElectronOrbitals.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<PeriodicTableScreen>:
    name: "periodic_table_screen"  

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "PeriodicTable.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<FormulaExplanation1Screen>:
    name: "formula_explanation_1_screen"  

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "EquationExplanations-1.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<FormulaExplanation2Screen>:
    name: "formula_explanation_2_screen"  

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "EquationExplanation-2.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<FormulaExplanation3Screen>:
    name: "formula_explanation_3_screen"    

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "body-ap-physics-1-wave-table.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<FormulaExplanation4Screen>:
    name: "formula_explanation_4_screen"   

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "body-ap-physics-1-trigonometry-table.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<IonizationEnergiesScreen>:
    name: "ionization_energies_screen"   

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "IonazationEnergies.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<PlanckCurvesScreen>:
    name: "planck_curves_screen"   

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "PlanckCurves.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<StandardModelScreen>:
    name: "standard_model_screen"   

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "StandardModel copy.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<AirResistanceCoefficientScreen>:
    name: "air_resistance_coefficient_screen"   

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "AirResistance.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right" 


<CosmicBackGroundRadiationScreen>:
    name: "cosmic_background_radiation_screen"   

    BoxLayout: 
        orientation: "vertical" 
        Image:
            source: "CosmicBackgroundRadiation.png"
            pos_hint: {'center_x': 0.5, "top": 1}
            allow_stretch: True    

        MDRaisedButton:
            text: 'Back'
            pos_hint: {'center_x': 0.5, "center_y":0.05}
            on_release: 
                #print("Click?")
                root.screen_manager.current = "resource_screen"
                root.screen_manager.transition.direction = "right"       


Screen:
    name : 'Physics Backpack'

    BoxLayout:
        orientation: 'vertical'

        MDToolbar:
            id: toolbar
            title: 'Physics Backpack'
            left_action_items: [["menu", lambda x:nav_drawer.set_state("open")]]
            elevation: 10

        MDNavigationLayout:
            x: toolbar.height

            ScreenManager:
                id: screen_manager

                Screen:
                    name: "main_screen"


                Screen:
                    name: "thermo_screen"

                    ScrollView:

                        MDList:


                            OneLineListItem:
                                text: "Acceleration"
                                on_release:
                                    #print("Click!")
                                    screen_manager.current = "acceleration_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Displacement"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "displacement_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Density"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "density_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Phase Velocity"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "phase_velocity_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Static Fluid Pressure"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "static_fluid_pressure_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Dynamic Pressure"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "dynamic_pressure_screen"
                                    screen_manager.transition.direction = "left"                                    

                            OneLineListItem:
                                text: "Buoyancy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "buoyancy_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Volumetric Flow Rate"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "volumetric_flow_rate_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Mass Flow Rate"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "mass_flow_rate_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Heat Capacity"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "heat_capacity_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Mechanical Advantage"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "mechanical_advantage_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Index of Refraction"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "index_of_refraction_screen"
                                    screen_manager.transition.direction = "left"       


                Screen:
                    name: "elec_screen"

                    ScrollView:

                        MDList:

                            OneLineListItem:
                                text: "Electric Power"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "electric_power_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Electric Current"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "electric_current_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Ohm's Law"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "ohm's_law_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Voltage"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "voltage_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Electric Field"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "electric_field_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Magnetic Flux"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "magnetic_flux_screen"
                                    screen_manager.transition.direction = "left"   

                            OneLineListItem:
                                text: "Magnetic Field"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "magnetic_field_screen"
                                    screen_manager.transition.direction = "left"                                 

                            OneLineListItem:
                                text: "Force of Magnetic Field"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "magnetic_force_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Resistivity"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "resistivity_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Capacitance"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "capacitance_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Capacitor Energy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "capacitor_energy_screen"
                                    screen_manager.transition.direction = "left"  

                            OneLineListItem:
                                text: "Inductor Energy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "inductor_energy_screen"
                                    screen_manager.transition.direction = "left"                      

                            OneLineListItem:
                                text: "Coulomb's Law"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "coulomb's_law_screen"
                                    screen_manager.transition.direction = "left"                                        


                Screen:
                    name: "motion_screen"

                    ScrollView:

                        MDList:

                            OneLineListItem:
                                text: "Newton's Second Law"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "newton's_second_law_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Gravitational Acceleration"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "gravitational_acceleration_screen"
                                    screen_manager.transition.direction = "left"                               

                            OneLineListItem:
                                text: "Hooke's Law"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "hooke's_law_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Momentum"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "momentum_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Work"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "work_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Kinetic Energy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "kinetic_energy_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Potential Energy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "potential_energy_screen"
                                    screen_manager.transition.direction = "left"                                    

                            OneLineListItem:
                                text: "Elastic Energy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "elastic_energy_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Energy Conversion Efficiency"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "energy_conversion_efficiency_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Pressure"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "pressure_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Pressure-Volume Work"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "pressure_volume_work_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Newton's Law of Universal Gravitation"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "newton's_law_of_universal_gravitation_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Centrifugal Force"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "centrifugal_force_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Friction"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "friction_screen"
                                    screen_manager.transition.direction = "left"       

                            OneLineListItem:
                                text: "Rotational Kinetic Energy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "rotational_kinetic_energy_screen"
                                    screen_manager.transition.direction = "left"     

                            OneLineListItem:
                                text: "Torque"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "torque_screen"
                                    screen_manager.transition.direction = "left"    


                Screen:
                    name: "atomic_screen"

                    ScrollView:

                        MDList:

                            OneLineListItem:
                                text: "Wavelength"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "wavelength_screen"
                                    screen_manager.transition.direction = "left"                                                                                                                                                                                                                                                                                                                                                          

                            OneLineListItem:
                                text: "De Broglie Wavelength"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "de_broglie_wavelength_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Mass-Energy Equivalence"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "mass_energy_equivalence_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Energy"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "energy_screen"
                                    screen_manager.transition.direction = "left"

                            OneLineListItem:
                                text: "Min. Energy to Eject Electron"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "ke_max_screen"
                                    screen_manager.transition.direction = "left" 


                Screen:
                    name: "resource_screen"

                    ScrollView:

                        MDList:

                            OneLineListItem:
                                text: "Constants"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "constants_screen"

                            OneLineListItem:
                                text: "Base Units"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "units_screen"

                            OneLineListItem:
                                text: "Periodic Table"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "periodic_table_screen"

                            OneLineListItem:
                                text: "Electron Orbitals"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "electron_orbitals_screen"

                            OneLineListItem:
                                text: "Ionization Energies"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "ionization_energies_screen"

                            OneLineListItem:
                                text: "Planck Curves"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "planck_curves_screen"

                            OneLineListItem:
                                text: "Standard Model"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "standard_model_screen"

                            OneLineListItem:
                                text: "Air Resistance Coefficient"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "air_resistance_coefficient_screen"

                            OneLineListItem:
                                text: "Cosmic Microwave Background"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "cosmic_background_radiation_screen"

                            OneLineListItem:
                                text: "Greek Alphabet"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "alphabet_screen"

                            OneLineListItem:
                                text: "Formula Explanation Mechanics"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "formula_explanation_1_screen"                                                                                                                                                                                                                                                                                                                                                                                                            

                            OneLineListItem:
                                text: "Formula Explanation Electricity"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "formula_explanation_2_screen"

                            OneLineListItem:
                                text: "Formula Explanation Waves"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "formula_explanation_3_screen"

                            OneLineListItem:
                                text: "Formula Explanation Trigonometry"
                                on_release: 
                                    #print("Click!")
                                    screen_manager.current = "formula_explanation_4_screen"


                AccelerationScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                DisplacementScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer      


                DensityScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                                  


                ConstantsScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer


                WavelengthScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                PhaseVelocityScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                StaticFluidPressureScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                DynamicPressureScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer               

                BuoyancyScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                VolumetricFlowRateScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                MassFlowRateScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                HeatCapacityScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                DeBroglieWavelengthScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                MechanicalAdvantageScreen:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                

                IndexOfRefractionScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer  

                NewtonsSecondLawScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer   

                GravitationalAccelerationScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                       

                NewtonsLawOfUniversalGravitationScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer   

                HookesLawScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                MomentumScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                WorkScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer  

                KineticEnergyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                     

                PotentialEnergyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer  

                ElasticEnergyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer  

                EnergyConversionEfficiencyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer   

                PressureScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer  

                PressureVolumeWorkScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                CentrifugalForceScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                CoulombsLawScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                FrictionScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                TorqueScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                RotationalKineticEnergyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                ElectricPowerScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                ElectricCurrentScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                OhmsLawScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                VoltageScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                ResistivityScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                CapacitanceScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                CapacitorEnergyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer      

                InductorEnergyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                EnergyScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                KEMaxScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                MassEnergyEquivalenceScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                ElectricFieldScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                MagneticFieldScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                MagneticFluxScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                MagneticForceScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                PeriodicTableScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                ElectronOrbitalsScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

                AlphabetScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer                        

                UnitsScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                FormulaExplanation1Screen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer           

                FormulaExplanation2Screen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                FormulaExplanation3Screen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer  

                FormulaExplanation4Screen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                IonizationEnergiesScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                PlanckCurvesScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                StandardModelScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                AirResistanceCoefficientScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 

                CosmicBackgroundRadiationScreen: 
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer 


            MDNavigationDrawer:
                id: nav_drawer  

                ContentNavigationDrawer:
                    screen_manager: screen_manager
                    nav_drawer: nav_drawer

"""


class CosmicBackgroundRadiationScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class AirResistanceCoefficientScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class StandardModelScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class PlanckCurvesScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class IonizationEnergiesScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FormulaExplanation4Screen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FormulaExplanation3Screen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FormulaExplanation2Screen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FormulaExplanation1Screen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class AlphabetScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class UnitsScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FormulaExplanationScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ElectronOrbitalsScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class PeriodicTableScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MagneticForceScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MagneticFluxScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MagneticFieldScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ElectricFieldScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MassEnergyEquivalenceScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class KEMaxScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class EnergyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class InductorEnergyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CapacitorEnergyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CapacitanceScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ResistivityScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class VoltageScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class OhmsLawScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ElectricCurrentScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ElectricPowerScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class RotationalKineticEnergyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class TorqueScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class FrictionScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CoulombsLawScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class CentrifugalForceScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class PressureVolumeWorkScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class PressureScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class EnergyConversionEfficiencyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ElasticEnergyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class PotentialEnergyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class KineticEnergyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class WorkScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MomentumScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class HookesLawScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class NewtonsLawOfUniversalGravitationScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class GravitationalAccelerationScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class NewtonsSecondLawScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class IndexOfRefractionScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MechanicalAdvantageScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class DeBroglieWavelengthScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class HeatCapacityScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MassFlowRateScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class VolumetricFlowRateScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class BuoyancyScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class DynamicPressureScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class StaticFluidPressureScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class PhaseVelocityScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class WavelengthScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class DensityScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ConstantsScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class AccelerationScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class DisplacementScreen(Screen):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


sm = ScreenManager()
sm.add_widget(CosmicBackgroundRadiationScreen(name="cosmic_background_radiation_screen"))
sm.add_widget(AirResistanceCoefficientScreen(name="air_resistance_coefficient_screen"))
sm.add_widget(StandardModelScreen(name="standard_model_screen"))
sm.add_widget(PlanckCurvesScreen(name="planck_curves_screen"))
sm.add_widget(IonizationEnergiesScreen(name="ionization_energies_screen"))
sm.add_widget(FormulaExplanation4Screen(name="formula_explanation_4_screen"))
sm.add_widget(FormulaExplanation3Screen(name="formula_explanation_3_screen"))
sm.add_widget(FormulaExplanation2Screen(name="formula_explanation_2_screen"))
sm.add_widget(FormulaExplanation1Screen(name="formula_explanation_1_screen"))
sm.add_widget(AlphabetScreen(name="alphabet_screen"))
sm.add_widget(UnitsScreen(name="units_screen"))
sm.add_widget(ElectronOrbitalsScreen(name="electron_orbitals_screen"))
sm.add_widget(PeriodicTableScreen(name="periodic_table_screen"))
sm.add_widget(MagneticForceScreen(name="magnetic_force_screen"))
sm.add_widget(MagneticFluxScreen(name="magnetic_flux_screen"))
sm.add_widget(MagneticFieldScreen(name="magnetic_field_screen"))
sm.add_widget(ElectricFieldScreen(name="electric_field_screen"))
sm.add_widget(KEMaxScreen(name="mass_energy_equivalence_screen"))
sm.add_widget(KEMaxScreen(name="ke_max_screen"))
sm.add_widget(EnergyScreen(name="energy_screen"))
sm.add_widget(InductorEnergyScreen(name="inductor_energy_screen"))
sm.add_widget(CapacitorEnergyScreen(name="capacitor_energy_screen"))
sm.add_widget(CapacitanceScreen(name="capacitance_screen"))
sm.add_widget(ResistivityScreen(name="resistivity_screen"))
sm.add_widget(VoltageScreen(name="voltage_screen"))
sm.add_widget(OhmsLawScreen(name="ohm's_law_screen"))
sm.add_widget(ElectricCurrentScreen(name="electric_current_screen"))
sm.add_widget(ElectricPowerScreen(name="electric_power_screen"))
sm.add_widget(RotationalKineticEnergyScreen(name="rotational_kinetic_energy_screen"))
sm.add_widget(TorqueScreen(name="torque_screen"))
sm.add_widget(FrictionScreen(name="friction_screen"))
sm.add_widget(CoulombsLawScreen(name="coulomb's_law_screen"))
sm.add_widget(CentrifugalForceScreen(name="centrifugal_force_screen"))
sm.add_widget(PressureVolumeWorkScreen(name="pressure_volume_work_screen"))
sm.add_widget(PressureScreen(name="pressure_screen"))
sm.add_widget(EnergyConversionEfficiencyScreen(name="energy_conversion_efficiency_screen"))
sm.add_widget(PotentialEnergyScreen(name="elastic_energy_screen"))
sm.add_widget(PotentialEnergyScreen(name="potential_energy_screen"))
sm.add_widget(KineticEnergyScreen(name="kinetic_energy_screen"))
sm.add_widget(WorkScreen(name="work_screen"))
sm.add_widget(MomentumScreen(name="momentum_screen"))
sm.add_widget(HookesLawScreen(name="hooke's_law_screen"))
sm.add_widget(NewtonsLawOfUniversalGravitationScreen(name="newton's_law_of_universal_gravitation_screen"))
sm.add_widget(GravitationalAccelerationScreen(name="gravitational_acceleration_screen"))
sm.add_widget(NewtonsSecondLawScreen(name="newton's_second_law_screen"))
sm.add_widget(MechanicalAdvantageScreen(name="index_of_refraction_screen"))
sm.add_widget(MechanicalAdvantageScreen(name="mechanical_advantage_screen"))
sm.add_widget(DeBroglieWavelengthScreen(name="de_broglie_wavelength_screen"))
sm.add_widget(HeatCapacityScreen(name="heat_capacity_screen"))
sm.add_widget(MassFlowRateScreen(name="mass_flow_rate_screen"))
sm.add_widget(VolumetricFlowRateScreen(name="volumetric_flow_rate_screen"))
sm.add_widget(BuoyancyScreen(name="buoyancy_screen"))
sm.add_widget(DynamicPressureScreen(name="dynamic_pressure_screen"))
sm.add_widget(StaticFluidPressureScreen(name="static_fluid_pressure_screen"))
sm.add_widget(PhaseVelocityScreen(name="phase_velocity_screen"))
sm.add_widget(WavelengthScreen(name="wavelength_screen"))
sm.add_widget(DensityScreen(name="density_screen"))
sm.add_widget(DisplacementScreen(name="displacement_screen"))
sm.add_widget(AccelerationScreen(name="acceleration_screen"))
sm.add_widget(ConstantsScreen(name="constants_screen"))


class PhysicsApp(MDApp):
    dialog = None

    def build(self):


        self.icon = 'imageonline-co-roundcorner.png'
        self.App = Builder.load_string(KV)
        self.title = 'Physics Backpack'


        self.constants_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'top': 0.95},
            size_hint=(0.95, 0.8),
            rows_num=22,
            column_data=[
                ("Symbol", dp(45)),
                ("Name", dp(45)),
                ("Value", dp(45))
            ],
            row_data=[
                ("c", "speed of light in a vacuum", "299,792,458 m/s"),
                ("R", "gas constant", "8.3144598 J/molK"),
                ("G", "gravitational constant", "6.67408x10^-11 Nm^2/kg^2"),
                ("h", "planck constant", "6.626070040x10^-34 Js"),
                ("hc", "physical", "1.98644582x10^-25 Jm"),
                ("ħ", "reduced plack constant", "1.054571800x10^-34 Js"),
                ("ε0", "electric constant", "8.85418782 × 10^-12 m^-3 kg^-1 s^4 A^2"),
                ("μ0", "magnetic constant", "1.25663706 × 10^-6 m kg s^-2 A^-2"),
                ("e", "elementary charge", "1.60217662 × 10^-19 C"),
                ("me", "electron mass", "9.10938356×10^−31 kg"),
                ("mp", "proton mass", "1.672621898x10^-27"),
                ("mn", "neutron mass", "1.674927471x10^-27 kg"),
                ("mu", "atomic mass constant", "1.660539040x10^-27 kg"),
                ("Na", "avogadro's constant", "6.022140857x10^23 mol^-1"),
                ("ΔνCs", "hyperfine transition frequency of Cs", "9,192,631,770 Hz"),
                ("Kcd", "luminous efficacy of 540 THz radiation", "683 lm/W"),
                ("k", "boltzmann's constant", "1.38064852x10^-23 J/K"),
                ("σ", "stefan-boltzmann constant", "5.670367x10^-8 W/m^2K^4"),
                ("b", "wien displacement constant", "2.8977729 mm/K"),
                ("g", "gravity on the surface of earth", "9,80665 m/s^2"),
                ("atm", "atmospheric pressure on earth", "101,325 Pa"),
                ("H0", "Hubble constant", "69.3 km/s/Mpc")
            ]
        )

        self.units_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'top': 0.95},
            size_hint=(0.95, 0.8),
            rows_num=15,
            column_data=[
                ("Measure", dp(30)),
                ("Name", dp(30)),
                ("Symbol", dp(30))
            ],
            row_data=[
                ("length", "meter", "m"),
                ("mass", "kilogram", "kg"),
                ("time", "second", "s"),
                ("electric current", "ampere", "A"),
                ("temperature", "kelvin", "K"),
                ("amount of substance", "mole", "mol"),
                ("luminous intensity", "candelas", "cd"),
                ("frequency", "hertz", "Hz"),
                ("force", "newton", "N"),
                ("work/energy", "joule", "J"),
                ("power", "watt", "W"),
                ("electric charge", "coulomb", "C"),
                ("voltage", "volt", "V"),
                ("electrical resistance", "ohm", "Ω"),
                ("temperature", "celcius", "°C")
            ]
        )

        self.alphabet_table = MDDataTable(
            pos_hint={'center_x': 0.5, 'top': 0.95},
            size_hint=(0.95, 0.8),
            rows_num=24,
            column_data=[
                ("Name", dp(30)),
                ("Uppercase", dp(30)),
                ("Lowercase", dp(30)),
                ("English Equivalent", dp(30))
            ],
            row_data=[
                ("Alpha", "Α", "α", "a"),
                ("Beta", "Β", "β", "b"),
                ("Gamma", "Γ", "γ", "g"),
                ("Delta", "Δ", "δ", "d"),
                ("Epsilon", "Ε", "ε", "e"),
                ("Zeta", "Ζ", "ζ", "z"),
                ("Eta", "Η", "η", "h"),
                ("Theta", "Θ", "θ", "th"),
                ("Lota", "Ι", "ι", "i"),
                ("Kappa", "Κ", "κ", "k"),
                ("Lambda", "Λ", "λ", "l"),
                ("Mu", "Μ", "μ", "m"),
                ("Nu", "Ν", "ν", "n"),
                ("Xi", "Ξ", "ξ", "x"),
                ("Omicron", "Ο", "o", "o"),
                ("Pi", "Π", "π", "p"),
                ("Rho", "Ρ", "ρ", "r"),
                ("Sigma", "Σ", "σ,ς", "s"),
                ("Tau", "Τ", "τ", "t"),
                ("Upsilon", "Υ", "υ", "u"),
                ("Phi", "Φ", "φ", "ph"),
                ("Chi", "Χ", "χ", "ch"),
                ("Psi", "Ψ", "ψ", "ps"),
                ("Omega", "Ω", "ω", "o")
            ]
        )
        # root = Builder.load_string(KV)
        self.App.ids.screen_manager.get_screen("constants_screen").ids.constants_table.add_widget(self.constants_table)
        self.App.ids.screen_manager.get_screen("units_screen").ids.units_table.add_widget(self.units_table)
        self.App.ids.screen_manager.get_screen("alphabet_screen").ids.alphabet_table.add_widget(self.alphabet_table)
        return self.App


    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Try Again",
                text="In order to calculate all the required fields must be filled, please fill and try again.",
            )

        self.dialog.open()


    def acceleration(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("acceleration_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("acceleration_screen").ids.time.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("acceleration_screen").ids.accel.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def accelvelocity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("acceleration_screen").ids.accel.text)
            val2 = float(self.App.ids.screen_manager.get_screen("acceleration_screen").ids.time.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("acceleration_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def acceltime(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("acceleration_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("acceleration_screen").ids.accel.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("acceleration_screen").ids.time.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def displacement(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("displacement_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("displacement_screen").ids.time.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("displacement_screen").ids.displacement.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def disvelocity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("displacement_screen").ids.displacement.text)
            val2 = float(self.App.ids.screen_manager.get_screen("displacement_screen").ids.time.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("displacement_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def distime(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("displacement_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("displacement_screen").ids.displacement.text)
            res = val2 / val1
            self.App.ids.screen_manager.get_screen("displacement_screen").ids.time.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def density(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("density_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("density_screen").ids.volume.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("density_screen").ids.density.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def denmass(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("density_screen").ids.volume.text)
            val2 = float(self.App.ids.screen_manager.get_screen("density_screen").ids.density.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("density_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def denvolume(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("density_screen").ids.density.text)
            val2 = float(self.App.ids.screen_manager.get_screen("density_screen").ids.mass.text)
            res = val2 / val1
            self.App.ids.screen_manager.get_screen("density_screen").ids.volume.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def wavelength(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("wavelength_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("wavelength_screen").ids.frequency.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("wavelength_screen").ids.wavelength.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def wavfrequency(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("wavelength_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("wavelength_screen").ids.wavelength.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("wavelength_screen").ids.frequency.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def wavvelocity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("wavelength_screen").ids.wavelength.text)
            val2 = float(self.App.ids.screen_manager.get_screen("wavelength_screen").ids.frequency.text)
            res = val2 * val1
            self.App.ids.screen_manager.get_screen("wavelength_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def phasewave(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.phase_velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.period.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.wavelength.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def phaseperiod(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.wavelength.text)
            val2 = float(self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.phase_velocity.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.period.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def phasevelocity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.wavelength.text)
            val2 = float(self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.period.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("phase_velocity_screen").ids.phase_velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def staticdensity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.pressure.text)
            val2 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.gravitational_acceleration.text)
            val3 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.depth.text)
            res = val1 / val2 * val3
            self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.density.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def staticgravity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.pressure.text)
            val2 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.depth.text)
            val3 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.density.text)
            res = val1 / val2 * val3
            self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.gravitational_acceleration.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def staticdepth(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.pressure.text)
            val2 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.gravitational_acceleration.text)
            val3 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.density.text)
            res = val1 / val2 * val3
            self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.depth.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def staticpressure(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.density.text)
            val2 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.gravitational_acceleration.text)
            val3 = float(self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.depth.text)
            res = val1 * val2 * val3
            self.App.ids.screen_manager.get_screen("static_fluid_pressure_screen").ids.pressure.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def dynamdensity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.flow_speed.text)
            val2 = float(self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.pressure.text)
            res = (val2 * 2) / (val1 * val1)
            self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.density.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def dynamflow(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.pressure.text)
            val2 = float(self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.density.text)
            res = math.sqrt((val2 * 2) / val1)
            self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.flow_speed.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def dynampressure(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.density.text)
            val2 = float(self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.flow_speed.text)
            res = ((val2 * val2) * val1) / 2
            self.App.ids.screen_manager.get_screen("dynamic_pressure_screen").ids.pressure.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def buoyancyden(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.buoyancy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.displaced_volume.text)
            val3 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.gravitational_acceleration.text)
            res = val1 / val2 * val3
            self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.density.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def buoyancydis(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.buoyancy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.gravitational_acceleration.text)
            val3 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.density.text)
            res = val1 / val2 * val3
            self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.displaced_volume.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def buoyancygra(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.buoyancy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.displaced_volume.text)
            val3 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.density.text)
            res = val1 / val2 * val3
            self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.gravitational_acceleration.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def buoyancy(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.density.text)
            val2 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.gravitational_acceleration.text)
            val3 = float(self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.displaced_volume.text)
            res = val1 * val2 * val3
            self.App.ids.screen_manager.get_screen("buoyancy_screen").ids.buoyancy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def volumetricflo(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.volumetric_flow_rate.text)
            val2 = float(self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.cross_sectional_vector_area.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.flow_velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def volumetriccro(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.volumetric_flow_rate.text)
            val2 = float(self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.flow_velocity.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen(
                "volumetric_flow_rate_screen").ids.cross_sectional_vector_area.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def volumetric(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.cross_sectional_vector_area.text)
            val2 = float(self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.flow_velocity.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("volumetric_flow_rate_screen").ids.volumetric_flow_rate.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def masschm(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.mass_flow_rate.text)
            val2 = float(self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.change_in_time.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.change_in_mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def masscht(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.mass_flow_rate.text)
            val2 = float(self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.change_in_mass.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.change_in_time.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def mass(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.change_in_mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.change_in_time.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("mass_flow_rate_screen").ids.mass_flow_rate.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def heatene(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.heat_capacity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.difference_in_temperature.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def heatdif(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.heat_capacity.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.difference_in_temperature.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def heat(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.difference_in_temperature.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("heat_capacity_screen").ids.heat_capacity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def devel(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.wavelength.text)
            res = (6.62607004 * (math.pow(10, -34))) / (val1 * val2)
            self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def demas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.wavelength.text)
            res = (6.62607004 * (math.pow(10, -34))) / (val1 * val2)
            self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def dewav(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.velocity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.mass.text)
            res = (6.62607004 * (math.pow(10, -34))) / (val1 * val2)
            self.App.ids.screen_manager.get_screen("de_broglie_wavelength_screen").ids.wavelength.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def mechanicalout(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.input_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.mechanical_advantage.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.output_force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def mechanicalinp(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.output_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.mechanical_advantage.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.input_force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def mechanical(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.output_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.input_force.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("mechanical_advantage_screen").ids.mechanical_advantage.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def indexspe(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("index_of_refraction_screen").ids.index_of_refraction.text)
            res = 299792458 / val1
            self.App.ids.screen_manager.get_screen("index_of_refraction_screen").ids.speed_of_light_in_medium.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def index(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("index_of_refraction_screen").ids.speed_of_light_in_medium.text)
            res = 299792458 / val1
            self.App.ids.screen_manager.get_screen("index_of_refraction_screen").ids.index_of_refraction.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def newtonacc(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.mass.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.acceleration.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def newtonmas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.acceleration.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def newtonfor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.acceleration.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("newton's_second_law_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def gravitationalfor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.gravitational_acceleration.text)
            val2 = float(self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.mass.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def gravitationalmas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.gravitational_acceleration.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def gravitational(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.mass.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("gravitational_acceleration_screen").ids.gravitational_acceleration.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def universalm1(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.distance_between_two_masses.text)
            val3 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_2.text)
            res = (val1 * (val2 * val2)) / ((6.67 * math.pow(10, -11)) * val3)
            self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_1.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def universalm2(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.distance_between_two_masses.text)
            val3 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_1.text)
            res = (val1 * (val2 * val2)) / ((6.67 * math.pow(10, -11)) * val3)
            self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_2.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def universaldis(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_1.text)
            val3 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_2.text)
            res = math.sqrt(((val2 * val3) / val1) * (6.67 * math.pow(10, -11)))
            self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.distance_between_two_masses.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def universalfor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_1.text)
            val2 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.mass_2.text)
            val3 = float(self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.distance_between_two_masses.text)
            res = ((val1 * val2) / (val3 * val3)) * (6.67 * math.pow(10, -11))
            self.App.ids.screen_manager.get_screen("newton's_law_of_universal_gravitation_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def hookesspr(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.deformation.text)
            res = val1 / -val2
            self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.spring_constant.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def hookesdef(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.spring_constant.text)
            res = val1 / -val2
            self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.deformation.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def hookesfor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.spring_constant.text)
            val2 = float(self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.deformation.text)
            res = -val1 * val2
            self.App.ids.screen_manager.get_screen("hooke's_law_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def momentummas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("momentum_screen").ids.momentum.text)
            val2 = float(self.App.ids.screen_manager.get_screen("momentum_screen").ids.velocity.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("momentum_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def momentumvel(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("momentum_screen").ids.momentum.text)
            val2 = float(self.App.ids.screen_manager.get_screen("momentum_screen").ids.mass.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("momentum_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def momentum(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("momentum_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("momentum_screen").ids.velocity.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("momentum_screen").ids.momentum.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def workfor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("work_screen").ids.work.text)
            val2 = float(self.App.ids.screen_manager.get_screen("work_screen").ids.displacement.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("work_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def workdis(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("work_screen").ids.work.text)
            val2 = float(self.App.ids.screen_manager.get_screen("work_screen").ids.force.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("work_screen").ids.displacement.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def work(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("work_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("work_screen").ids.displacement.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("work_screen").ids.work.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def kineticmas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.kinetic_energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.velocity.text)
            res = (val1 * 2) / (val2 * val2)
            self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def kineticvel(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.kinetic_energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.mass.text)
            res = math.sqrt((val1 * 2) / val2)
            self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def kinetic(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.velocity.text)
            res = 0.5 * val1 * (val2 * val2)
            self.App.ids.screen_manager.get_screen("kinetic_energy_screen").ids.kinetic_energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def potentialmas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.potential.text)
            val2 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.gravitational_acceleration.text)
            val3 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.height.text)
            res = val1 / (val2 * val3)
            self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def potentialgra(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.potential.text)
            val2 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.height.text)
            val3 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.mass.text)
            res = val1 / (val2 * val3)
            self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.gravitational_acceleration.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def potentialhei(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.potential.text)
            val2 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.mass.text)
            val3 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.gravitational_acceleration.text)
            res = val1 / (val2 * val3)
            self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.height.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def potential(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.height.text)
            val3 = float(self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.gravitational_acceleration.text)
            res = val1 * val2 * val3
            self.App.ids.screen_manager.get_screen("potential_energy_screen").ids.potential.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def elasticspr(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.elastic_energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.deformation.text)
            res = (val1 * 2) / (val2 * val2)
            self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.spring_constant.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def elasticdef(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.elastic_energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.spring_constant.text)
            res = math.sqrt((val1 * 2) / val2)
            self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.deformation.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def elastic(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.spring_constant.text)
            val2 = float(self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.deformation.text)
            res = 0.5 * val1 * (val2 * val2)
            self.App.ids.screen_manager.get_screen("elastic_energy_screen").ids.elastic_energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def energyout(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.efficiency.text)
            val2 = float(self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.input_power.text)
            res = (val1 / 100) * val2
            self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.output_power.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def energyin(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.efficiency.text)
            val2 = float(self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.output_power.text)
            res = (val2 / val1) / 100
            self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.input_power.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def energyeff(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.output_power.text)
            val2 = float(self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.input_power.text)
            res = (val1 / val2) * 100
            self.App.ids.screen_manager.get_screen("energy_conversion_efficiency_screen").ids.efficiency.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def pressurefor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("pressure_screen").ids.pressure.text)
            val2 = float(self.App.ids.screen_manager.get_screen("pressure_screen").ids.area.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("pressure_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def pressureare(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("pressure_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("pressure_screen").ids.pressure.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("pressure_screen").ids.area.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def pressure(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("pressure_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("pressure_screen").ids.area.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("pressure_screen").ids.pressure.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def pvpressure(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.pv_work.text)
            val2 = float(self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.volume.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def pvvolume(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.pv_work.text)
            val2 = float(self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.pressure.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.area.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def pvwork(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.pressure.text)
            val2 = float(self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.volume.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("pressure_volume_work_screen").ids.pv_work.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def centrifugalmas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.radius.text)
            val3 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.velocity.text)
            res = (val1 * val2) / (val3 * val3)
            self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def centrifugalvel(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.radius.text)
            val3 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.mass.text)
            res = math.sqrt((val1 * val2) / val3)
            self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def centrifugalrad(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.mass.text)
            val3 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.velocity.text)
            res = (val2 * (val3 * val3)) / val1
            self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.radius.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def centrifugal(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.velocity.text)
            val3 = float(self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.radius.text)
            res = (val1 * (val2 * val2)) / val3
            self.App.ids.screen_manager.get_screen("centrifugal_force_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def coulombc1(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.distance.text)
            val3 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_2.text)
            res = (val1 * (val2 * val2)) / ((8.9875517923 * math.pow(10, 9)) * val3)
            self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_1.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def coulombc2(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.distance.text)
            val3 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_1.text)
            res = (val1 * (val2 * val2)) / ((8.9875517923 * math.pow(10, 9)) * val3)
            self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_2.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def coulombdis(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_1.text)
            val3 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_2.text)
            res = math.sqrt(((val2 * val3) / val1) * (6.67 * math.pow(10, -11)))
            self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.distance.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def coulombfor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_1.text)
            val2 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.charge_2.text)
            val3 = float(self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.distance.text)
            res = ((val1 * val2) / (val3 * val3)) * (6.67 * math.pow(10, -11))
            self.App.ids.screen_manager.get_screen("coulomb's_law_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def frictioncoe(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("friction_screen").ids.friction.text)
            val2 = float(self.App.ids.screen_manager.get_screen("friction_screen").ids.normal_force.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("friction_screen").ids.friction_coefficient.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def frictionnor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("friction_screen").ids.friction.text)
            val2 = float(self.App.ids.screen_manager.get_screen("friction_screen").ids.friction_coefficient.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("friction_screen").ids.normal_force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def friction(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("friction_screen").ids.normal_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("friction_screen").ids.friction_coefficient.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("friction_screen").ids.friction.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def torquerad(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.torque.text)
            val3 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.angle.text)
            res = val2 / (val1 * (math.sin(val3)))
            self.App.ids.screen_manager.get_screen("torque_screen").ids.radius.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def torquefor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.torque.text)
            val2 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.radius.text)
            val3 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.angle.text)
            res = val1 / (val2 * (math.sin(val3)))
            self.App.ids.screen_manager.get_screen("torque_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def torqueang(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.torque.text)
            val2 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.force.text)
            val3 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.radius.text)
            res = math.asin(val1 / (val2 * val3))
            self.App.ids.screen_manager.get_screen("torque_screen").ids.angle.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def torque(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.angle.text)
            val3 = float(self.App.ids.screen_manager.get_screen("torque_screen").ids.radius.text)
            res = val1 * val3 * math.sin(val2)
            self.App.ids.screen_manager.get_screen("torque_screen").ids.torque.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def rotationalang(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.rotational_kinetic_energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.angular_velocity.text)
            res = (val1 * 2) / (val2 * val2)
            self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.moment_of_inertia.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def rotationalmom(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.rotational_kinetic_energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.moment_of_inertia.text)
            res = math.sqrt((val1 * 2) / val2)
            self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.angular_velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def rotational(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.moment_of_inertia.text)
            val2 = float(self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.angular_velocity.text)
            res = 0.5 * val1 * (val2 * val2)
            self.App.ids.screen_manager.get_screen("rotational_kinetic_energy_screen").ids.rotational_kinetic_energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def powercur(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_power_screen").ids.power.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_power_screen").ids.voltage.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("electric_power_screen").ids.current.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def powervol(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_power_screen").ids.power.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_power_screen").ids.current.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("electric_power_screen").ids.voltage.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def power(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_power_screen").ids.voltage.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_power_screen").ids.current.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("electric_power_screen").ids.power.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def currentcha(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_current_screen").ids.current.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_current_screen").ids.time.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("electric_current_screen").ids.charge.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def currenttim(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_current_screen").ids.charge.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_current_screen").ids.current.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("electric_current_screen").ids.time.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def current(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_current_screen").ids.charge.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_current_screen").ids.time.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("electric_current_screen").ids.current.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def ohmsvoltage(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.current.text)
            val2 = float(self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.resistance.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.voltage.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def ohmsresistance(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.voltage.text)
            val2 = float(self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.current.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.resistance.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def ohmscurrent(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.voltage.text)
            val2 = float(self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.resistance.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("ohm's_law_screen").ids.current.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def voltageene(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("voltage_screen").ids.voltage.text)
            val2 = float(self.App.ids.screen_manager.get_screen("voltage_screen").ids.charge.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("voltage_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def voltagecha(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("voltage_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("voltage_screen").ids.voltage.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("voltage_screen").ids.charge.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def voltage(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("voltage_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("voltage_screen").ids.charge.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("voltage_screen").ids.voltage.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def resistivitylen(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistivity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.area.text)
            val3 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistance.text)
            res = (val1 * val2) / val3
            self.App.ids.screen_manager.get_screen("resistivity_screen").ids.length.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def resistivityare(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistance.text)
            val2 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.length.text)
            val3 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistivity.text)
            res = (val1 * val2) / val3
            self.App.ids.screen_manager.get_screen("resistivity_screen").ids.area.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def resistivityres(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistivity.text)
            val2 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.area.text)
            val3 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.length.text)
            res = (val1 * val2) / val3
            self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistance.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def resistivity(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistance.text)
            val2 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.length.text)
            val3 = float(self.App.ids.screen_manager.get_screen("resistivity_screen").ids.area.text)
            res = (val1 * val2) / val3
            self.App.ids.screen_manager.get_screen("resistivity_screen").ids.resistivity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def capacitancecha(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("capacitance_screen").ids.voltage.text)
            val2 = float(self.App.ids.screen_manager.get_screen("capacitance_screen").ids.capacitance.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("capacitance_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def capacitancevol(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("capacitance_screen").ids.charge.text)
            val2 = float(self.App.ids.screen_manager.get_screen("capacitance_screen").ids.capacitance.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("capacitance_screen").ids.charge.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def capacitance(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("capacitance_screen").ids.charge.text)
            val2 = float(self.App.ids.screen_manager.get_screen("capacitance_screen").ids.voltage.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("capacitance_screen").ids.capacitance.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def capacitorcap(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.voltage.text)
            res = (val1 * 2) / (val2 * val2)
            self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.capacitance.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def capacitorvol(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.capacitance.text)
            res = math.sqrt((val1 * 2) / val2)
            self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.voltage.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def capacitorene(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.capacitance.text)
            val2 = float(self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.voltage.text)
            res = 0.5 * val1 * (val2 * val2)
            self.App.ids.screen_manager.get_screen("capacitor_energy_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def inductorind(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.current.text)
            res = (val1 * 2) / (val2 * val2)
            self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.inductance.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def inductorcur(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.inductance.text)
            res = math.sqrt((val1 * 2) / val2)
            self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.current.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def inductorene(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.inductance.text)
            val2 = float(self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.current.text)
            res = 0.5 * val1 * (val2 * val2)
            self.App.ids.screen_manager.get_screen("inductor_energy_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def energymas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("energy_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("energy_screen").ids.momentum.text)
            res = (val1 - (val2 * 299792458)) / (math.pow(299792458, 2))
            self.App.ids.screen_manager.get_screen("energy_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def energymom(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("energy_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("energy_screen").ids.mass.text)
            res = (val1 - (val2 * math.pow(299792458, 2))) / 299792458
            self.App.ids.screen_manager.get_screen("energy_screen").ids.momentum.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def energy(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("energy_screen").ids.mass.text)
            val2 = float(self.App.ids.screen_manager.get_screen("energy_screen").ids.momentum.text)
            res = math.sqrt(math.pow((val2 * 299792458), 2) + math.pow((val1 * math.pow(299792458, 2)), 2))
            self.App.ids.screen_manager.get_screen("energy_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def kefre(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("ke_max_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("ke_max_screen").ids.work_function.text)
            res = (val1 + val2) / (6.67 * math.pow(10, -11))
            self.App.ids.screen_manager.get_screen("ke_max_screen").ids.frequency.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def kewor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("ke_max_screen").ids.energy.text)
            val2 = float(self.App.ids.screen_manager.get_screen("ke_max_screen").ids.frequency.text)
            res = -val1 + ((6.67 * math.pow(10, -11)) * val2)
            self.App.ids.screen_manager.get_screen("ke_max_screen").ids.work_function.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def keene(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("ke_max_screen").ids.frequency.text)
            val2 = float(self.App.ids.screen_manager.get_screen("ke_max_screen").ids.work_function.text)
            res = ((6.67 * math.pow(10, -11)) * val1) - val2
            self.App.ids.screen_manager.get_screen("ke_max_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def massmas(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mass_energy_equivalence_screen").ids.energy.text)
            res = val1 / math.pow(299792458, 2)
            self.App.ids.screen_manager.get_screen("mass_energy_equivalence_screen").ids.mass.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def massene(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("mass_energy_equivalence_screen").ids.mass.text)
            res = val1 * math.pow(299792458, 2)
            self.App.ids.screen_manager.get_screen("mass_energy_equivalence_screen").ids.energy.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def electricfor(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_field_screen").ids.electric_field.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_field_screen").ids.charge.text)
            res = val1 * val2
            self.App.ids.screen_manager.get_screen("electric_field_screen").ids.force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def electriccha(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_field_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_field_screen").ids.electric_field.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("electric_field_screen").ids.charge.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def electricfie(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("electric_field_screen").ids.force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("electric_field_screen").ids.charge.text)
            res = val1 / val2
            self.App.ids.screen_manager.get_screen("electric_field_screen").ids.electric_field.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def magneticcur(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.magnetic_field.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.distance_from_wire.text)
            res = (val1 * val2 * 2 * math.pi) / 1.25663706212
            self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.current.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def magneticdis(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.magnetic_field.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.current.text)
            res = (val2 * 1.25663706212) / (2 * math.pi * val1)
            self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.distance_from_wire.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def magneticfie(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.current.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.distance_from_wire.text)
            res = (val1 * 1.25663706212) / (2 * math.pi * val2)
            self.App.ids.screen_manager.get_screen("magnetic_field_screen").ids.magnetic_field.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def fluxare(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.angle.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_field.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_flux.text)
            res = val3 / (val2 * math.cos(val1))
            self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.area.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def fluxmag(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_flux.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.area.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.angle.text)
            res = val1 / (val2 * math.cos(val3))
            self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_field.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def fluxang(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_flux.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.area.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_field.text)
            res = math.acos(val1 / (val2 * val3))
            self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.angle.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def flux(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_field.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.angle.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.area.text)
            res = val1 * val3 * math.cos(val2)
            self.App.ids.screen_manager.get_screen("magnetic_flux_screen").ids.magnetic_flux.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()


    def forcecha(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_field.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.velocity.text)
            val4 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.angle.text)
            res = val1 / (val2 * val3 * math.sin(val4))
            self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.charge.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def forcefie(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.charge.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.velocity.text)
            val4 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.angle.text)
            res = val1 / (val2 * val3 * math.sin(val4))
            self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_field.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def forceang(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.charge.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.velocity.text)
            val4 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_field.text)
            res = math.asin(val1 / (val2 * val3 * val4))
            self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.angle.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def forcevel(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_force.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.angle.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.charge.text)
            val4 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_field.text)
            res = val1 / (val2 * val3 * math.sin(val4))
            self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.velocity.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

    def force(self):
        try:
            val1 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_field.text)
            val2 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.angle.text)
            val3 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.charge.text)
            val4 = float(self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.velocity.text)
            res = val3 * val1 * val4 * math.sin(val2)
            self.App.ids.screen_manager.get_screen("magnetic_force_screen").ids.magnetic_force.text = f"{res}"
        except ValueError:
            self.show_alert_dialog()

PhysicsApp().run()

