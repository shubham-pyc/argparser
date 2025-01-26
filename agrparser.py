import sys

class ArgParser():
    def get_default_properties(self,required=False, help="", type=bool):
        return {
            "required":required,
            "help":help,
            "type":type,
            

        }
    def __init__(self):
        self.arguments = {}  
        self.required = set()
        self.flags = {}

    def add_arguments(self,name,type=bool, required=False, help="help text"):
        if name[0:2] != '--':
            raise Exception("Invalid name of the argument {} should start with --".format(name))
        name = name[2:]
        self.arguments[name] = self.get_default_properties(required=required, type=type)
        if required:
            self.required.add(name)
        if type == bool:
            self.flags[name[0]] = name
        
    def _invalid_arguemnt(self, name):
        raise Exception("Invalid arugment {}".format(name))

    def _parse_boolean(self,pointer, args):
        value = True
        to_add = 1
        if pointer + 1 < len(args):
            next_value = args[pointer + 1]
            if not next_value.startswith("-"):
                if value == '0':
                    value = False
                to_add += 1

        return value, to_add

    def _parse_argument(self, pointer, args, name,value_type): 
        
        if pointer + 1 < len(args):
            value = args[pointer + 1]
            try:
                return value_type(value), 2
            except Exception as e:
                raise ValueError("Invalid value: f{value} for type {value_type}")
             
        else:
            raise ValueError("value of arugment {} not found".format(name))
        
    
    def _validate_required_arguments(self,ret_value):
        diff = self.required - set(ret_value.keys())
        if len(diff) != 0:
            raise ValueError("Required arguments not passed", diff)
    
    
    def parse(self):
        args = sys.argv[1:]
        ret_value = {}
        pointer = 0

        while pointer <len(args):
            each = args[pointer]
            if each.startswith("--"):
                name = each[2:]
                if name not in self.arguments:
                    self._invalid_arguemnt(name)

                value_type = self.arguments.get(name)["type"]
                if value_type!= bool:
                    value, to_add = self._parse_argument(ret_value, args, name,value_type)
                    ret_value[name] = value
                    pointer += to_add
                else:
                    value, to_add = self._parse_boolean(pointer, args)
                    pointer += to_add
                    ret_value[name] = value

            elif each.startswith("-"):
                name = each[1:]
                
                for each in name:
                    if each not in self.flags:
                        raise ValueError("Invalid flag : -{} ".format(each))

                    full_name = self.flags[each]
                    value, to_add = self._parse_boolean(pointer, args)
                    # pointer += to_add
                    ret_value[full_name] = value
                pointer += 1
            else:
                self._invalid_arguemnt(name)

        self._validate_required_arguments(ret_value)

        return ret_value


## pass case
sys.argv = ['','--shubham','c']
c = ArgParser()
c.add_arguments("--shubham", type=str, required=True)
c.add_arguments("--gupta", type=int)
c.add_arguments("--flag", type=bool)
c.add_arguments("--cc", type=bool)
argss =c.parse()
assert argss["shubham"] == 'c'



sys.argv = ['','--shubham','c', '--gupta','0', '-fc']
c = ArgParser()
c.add_arguments("--shubham", type=str, required=True)
c.add_arguments("--gupta", type=int)
c.add_arguments("--flag", type=bool)
c.add_arguments("--cc", type=bool)
argss =c.parse()
assert argss["shubham"] == 'c' and argss['gupta'] == 0 and argss['flag'] == True and argss['cc'] == True



sys.argv = ['','--shubham','c', '--gupta','shubham', '-f']
c = ArgParser()
c.add_arguments("--shubham", type=str, required=True)
c.add_arguments("--gupta", type=int)
c.add_arguments("--flag", type=bool)
c.add_arguments("--cc", type=bool)
try:
    argss =c.parse()
except ValueError as e: 
    # print(str(e))
    assert str(e) == "invalid literal for int() with base 10: 'shubham'"





#Features

# parser = ArgParser(description="Hello world")
#parser.add("name", type=str, help="this is for help")
#parser.add("-a", "--age",type=int,help="something")