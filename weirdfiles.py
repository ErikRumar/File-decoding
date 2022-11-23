



def interpret_information(objects, list3):
    
    amounts = count_attributes(list3)

    # total = len(list3)
    # index = -1
    # for a in amounts:
    #     index += 1
    #     print(elements[index], ":", a)

    skin_colors = []
    reborn = 0
    death_before_birth = 0
    hgt_americans = 0
    ecl_green = 0
    ecl_grey = 0
    ecl_blue = 0
    ecl_brown = 0
    hzl = 0
    ecl_amb = 0
    cid_none = 0
    no_eyes = 0
    pid_cm = 0
    never_born = 0

    for obj in objects:

        
        if obj.byr != None and obj.iyr != None and obj.eyr != None :
            if obj.iyr < obj.byr and obj.iyr > obj.eyr:
                reborn += 1

        
        if obj.byr == None:
            never_born += 1

        skin_colors.append(obj.hcl)

        if obj.byr != None and obj.eyr != None :
            if obj.byr > obj.eyr:
                death_before_birth += 1

        if obj.hgt != None:
            for char in obj.hgt:
                if char == "n":
                    hgt_americans += 1


        if obj.ecl == "grn":
            ecl_green += 1
        elif obj.ecl == "gry":
            ecl_grey += 1
        elif obj.ecl == "amb":
            ecl_amb += 1
        elif obj.ecl == "blu":
            ecl_blue += 1
        elif obj.ecl == "hzl":
            hzl += 1
        elif obj.ecl == "brn":
            ecl_brown += 1
        else:
            no_eyes += 1

        if obj.cid == None:
            cid_none += 1

        if obj.pid != None:
            print(obj.pid[len(str(obj.pid))-3:])
            if obj.pid[len(str(obj.pid))-2:] == "cm":
                pid_cm += 1
    
    amountof_skin_colors = len(skin_colors)

    string = f"""

    ________________________Interpreted statistics__________________________
    
    Eyecolor:
    brown: {ecl_brown}
    blue: {ecl_blue}
    green: {ecl_brown}
    grey: {ecl_blue}
    ambient...?: {ecl_brown}
    hzl??: {hzl}

    {no_eyes} people sadly have apperantly no eyes

    they all have a total of {amountof_skin_colors} unique skin colors

    {cid_none} people are homeless (I suppose)

    {pid_cm} identify themselves with their height, (p)ersonal id

    {hgt_americans} people are stupid americans that measure in inches

    {death_before_birth} people died before they were born

    {reborn} people were accidentally reborn because of the incident

    {never_born} people were actually never born in the first place
    
    
    
    
    """
            
    return string

def count_attributes(object_list):
    iyr = 0
    hcl = 0
    ecl = 0
    byr = 0
    hgt = 0
    eyr = 0
    cid = 0
    pid = 0

    for obj in object_list:
        for attribute in obj:
            if attribute[:3] == "iyr":
                iyr += 1
            if attribute[:3] == "hcl":
                hcl += 1
            if attribute[:3] == "ecl":
                ecl += 1
            if attribute[:3] == "byr":
                byr += 1
            if attribute[:3] == "hgt":
                hgt += 1
            if attribute[:3] == "eyr":
                eyr += 1
            if attribute[:3] == "cid":
                cid += 1
            if attribute[:3] == "pid":
                pid += 1
    return [iyr, hcl, ecl, byr, hgt, eyr, cid, pid]

objects = []
class Object:

    def __init__(self, iyr, hcl, ecl, byr, hgt, eyr, cid, pid):
        self.iyr = iyr
        self.hcl = hcl
        self.ecl = ecl
        self.byr = byr
        self.hgt = hgt
        self.eyr = eyr
        self.cid = cid
        self.pid = pid

    def str1(self, index):

        string = f"""
        
        Object {index}:

        height: {self.hgt}
        birth year: {self.byr}
        incident year: {self.iyr}
        death year: {self.eyr}
        skin color: {self.hcl}
        eye color: {self.ecl}
        city id: {self.cid}
        personal id: {self.pid}


        
        """

        return string

with open("inputdec04.txt", "r", encoding= "utf8") as file:
    print("1")
    string = ""
    for line in file.readlines():
        string += line
    list1 = string.split("\n\n")
    print(list1)
    print("2")
    list2 = []
    for a in list1:
        x = a.replace("\n", " ")
        list2.append(x)
    print(list2)
    print("3")
    list3 = []
    for a in list2:
        attributes = a.split(" ")
        list3.append(attributes)
    print(list3)
    print("4")
    elements = ["iyr", "hcl", "ecl", "byr", "hgt", "eyr", "cid", "pid"]
    for a in list3:
        attributes = ["iyr", "hcl", "ecl", "byr", "hgt", "eyr", "cid", "pid"]
        for att in a:
            add = False
            index = -1
            for char in att:
                index += 1
                if add == True:
                    pass
                if char == ":":
                    types = att[:index]
                    attribute = att[index+1:]
                    add = True

            index = -1
            for a in elements:
                index += 1
                if a == types:
                    attributes[index] = attribute

        iyr = attributes[0]
        hcl = attributes[1]
        ecl = attributes[2]
        byr = attributes[3]
        hgt = attributes[4]
        eyr = attributes[5]
        cid = attributes[6]
        pid = attributes[7]

        if iyr == "iyr":
            iyr = None
        if hcl == "hcl":
            hcl = None
        if ecl == "ecl":
            ecl = None
        if byr == "byr":
            byr = None
        if hgt == "hgt":
            hgt = None
        if eyr == "eyr":
            eyr = None
        if cid == "cid":
            cid = None
        if pid == "pid":
            pid = None
            
        objects.append(Object(iyr, hcl, ecl, byr, hgt, eyr, cid, pid))


index = -1
for o in objects:
    index += 1
    print(o.str1(index))


print(interpret_information(objects, list3))