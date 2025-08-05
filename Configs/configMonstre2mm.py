from fullcontrol import *
import fullcontrol as fc

def getInit():
    # create the initialize procedure (i.e. start_gcode)
    initialization_data = {
        "print_speed": 1000, #1000mm/min = 16mm/s donc 100mm/s=6000mm/min
        "travel_speed": 2000,
        "area_model": "rectangle",
        "extrusion_width": 2,
        "extrusion_height": 2,
        "print_speed_percent": 100,
        "material_flow_percent": 100,
        "e_units": "mm",
        "relative_e": True,
        "relative_e": True,
        "dia_feed": 1.6,
        "printer_command_list": {
            "home": "G28 ; home axes",
            "retract": "G10 ; retract",
            "unretract": "G11 ; unretract",
            "absolute_coords": "G90 ; absolute coordinates",
            "relative_coords": "G91 ; absolute coordinates",
            "units_mm": "G21 ; set units to millimeters"
        }
    }



    gcode_controls = GcodeControls(printer_name='custom', initialization_data=initialization_data)
    starting_procedure_steps = []
    #starting_procedure_steps.append(ManualGcode(text="M42 P5 S1"))
    starting_procedure_steps.append(ManualGcode(text="G92 X0 Y0 Z5"))
    #starting_procedure_steps.append(ManualGcode(text="M42 P3 S0.2"))
    starting_procedure_steps.append(PrinterCommand(id='absolute_coords'))
    starting_procedure_steps.append(PrinterCommand(id='units_mm'))
    starting_procedure_steps.append(Extruder(relative_gcode=initialization_data["relative_e"]))
    #starting_procedure_steps.append(ManualGcode(
    #    text='M220 S' + str(initialization_data["print_speed_percent"])+' ; set speed factor override percentage'))
    #starting_procedure_steps.append(ManualGcode(
    #    text='M221 S' + str(initialization_data["material_flow_percent"])+' ; set extrude factor override percentage'))
    starting_procedure_steps.append(Extruder(on=False))
    starting_procedure_steps.append(Point(x=0, y=0, z=5))
    starting_procedure_steps.append(Extruder(on=True))
    starting_procedure_steps.append(ManualGcode(text=';-----\n; END OF STARTING PROCEDURE\n;-----\n'))

    # move the home command in the start procedure to be after temperatures (to work with bed levelling)
    del starting_procedure_steps[1]
    starting_procedure_steps.insert(6, GcodeComment(end_of_previous_line_text='; including mesh bed level'))

    ending_procedure_steps = []
    ending_procedure_steps.append(ManualGcode(text='\n;-----\n; START OF ENDING PROCEDURE\n;-----'))
    ending_procedure_steps.append(ManualGcode(text='G91 ; relative coordinates'))
    ending_procedure_steps.append(ManualGcode(text='G0 Z20 F8000 ; drop bed'))
    ending_procedure_steps.append(ManualGcode(text='G90 ; absolute coordinates'))
    ending_procedure_steps.append(ManualGcode(text='M42 P5 S0; pump off'))
    ending_procedure_steps.append(Fan(speed_percent=0))
  


    return gcode_controls,starting_procedure_steps,ending_procedure_steps


def getGcode(steps):
    gcode_controls,starting_procedure_steps,ending_procedure_steps = getInit()
    steps = starting_procedure_steps + steps + ending_procedure_steps
    #open(name+'.gcode', 'w').write(transform(steps, 'gcode', gcode_controls))
    fc.transform(steps,'plot',fc.PlotControls(color_type='print_sequence'))
    return transform(steps, 'gcode', gcode_controls)

def plotGcode(steps, output_file="visualisation.html"):
    gcode_controls, starting_procedure_steps, ending_procedure_steps = getInit()
    steps = starting_procedure_steps + steps + ending_procedure_steps
    """html = fc.transform(steps, 'html', gcode_controls)
    with open(output_file, "w") as f:
        f.write(html)"""
    return fc.transform(steps, 'html', gcode_controls)