from Adafruit_LED_Backpack import SevenSegment

# ===========================================================================
# Clock Example
# ===========================================================================
segment = SevenSegment.SevenSegment(address=0x70)
colonBool = True
# Initialize the display. Must be called once before using the display.
segment.begin()
def writeToDisplay(value):
    global segment
    global colonBool
    try:
        #print "Writing to display:" + value
        segment.print_number_str(value)
        segment.set_colon(colonBool)
        segment.write_display()
        if(colonBool):
            colonBool = False
        else:
            colonBool = True
    except BaseException as ex:
        print("Error Writing to display:" + str(ex.message))

def clear():
	segment.clear()     
