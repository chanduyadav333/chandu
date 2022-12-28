class Lift:
    def __init__(self):
        self.current_lift_position = 0
    def lift_calling(self,lift_call):
        self.lift_call = lift_call
        if(self.lift_call == self.current_lift_position):
            print("current lift possion",self.current_lift_position)
        elif(self.lift_call>self.current_lift_position):
            for i in range(self.current_lift_position,self.lift_call+1):
               self.current_lift_position=i
               print("current lift possion", self.current_lift_position)
        else:
            for i in range(self.current_lift_position-1,self.lift_call-1,-1):
                self.current_lift_position = i
                print("current lift possion", self.current_lift_position)
    def destination(self,destination_point):
        self.destination_point = destination_point
        if (self.destination_point == self.current_lift_position):
            print("current lift possion", self.current_lift_position)
            print("this is the destination")
        elif (self.destination_point > self.current_lift_position):
            for i in range(self.current_lift_position, self.destination_point + 1):
                self.current_lift_position = i
                print("current lift possion", self.current_lift_position)
                if self.destination_point == self.current_lift_position:
                    print("this is the destination")
        else:
            for i in range(self.current_lift_position - 1, self.destination_point - 1, -1):
                self.current_lift_position = i
                print("current lift possion", self.current_lift_position)
                if self.destination_point == self.current_lift_position:
                    print("this is the destination")




lift_obj = Lift()
lift_obj.lift_calling(5)
lift_obj.destination(4)
lift_obj.destination(7)
lift_obj.lift_calling(1)
lift_obj.destination(7)
