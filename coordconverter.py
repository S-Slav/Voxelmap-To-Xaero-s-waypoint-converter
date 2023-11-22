import os
for file in os.listdir():
    if file.endswith(".points"):
        pointsfile=file
        worldname=(pointsfile.partition(".points")[0])
        listOfCoords=[]
        with open(pointsfile,"r")as r:
            for line in r.readlines():
                listOfCoords.append(line)

        waypointo = []
        waypointn = []
        waypointe = []

        for coord in listOfCoords :
            
            coordinates=coord.split(":")
            if coordinates[0]=="name":
                name=(coordinates[1].partition(",")[0])
                x=(coordinates[2].partition(",")[0])
                y=(coordinates[4].partition(",")[0])
                z=(coordinates[3].partition(",")[0])
                appndstr="waypoint:"+name+":"+name[0].upper()+":"+x+":"+y+":"+z+":""2:false:0:gui.xaero_default:false:0:false\n"
                if coordinates[11]  == 'the_nether#\n' or coordinates[11]  == 'the_nether#*':
                    waypointn.append(appndstr)
                elif coordinates[11]  == 'the_end#\n' or coordinates[11]  == 'the_end#*':
                    waypointe.append(appndstr)
                else:
                    waypointo.append(appndstr)
            
            if not os.path.isdir('XaeroWaypoints'):
                os.mkdir('XaeroWaypoints')
            worldname_path = os.path.join('XaeroWaypoints', worldname)
            if not os.path.isdir(worldname_path):
                os.mkdir(worldname_path)
            dim0path = os.path.join(worldname_path, 'dim%0')
            if not os.path.isdir(dim0path):
                os.mkdir(dim0path)
            dimn1path = os.path.join(worldname_path, 'dim%-1')
            if not os.path.isdir(dimn1path):
                os.mkdir(dimn1path)
            dim1path = os.path.join(worldname_path, 'dim%1')
            if not os.path.isdir(dim1path):
                os.mkdir(dim1path)
            opath = os.path.join(dim0path,'waypoints.txt')
            with open(opath,"w")as o:
                for i in waypointo:
                    o.write(i)
            npath = os.path.join(dimn1path,'waypoints.txt')
            with open(npath,"w")as n:
                for j in waypointn:
                    n.write(j)    
            epath = os.path.join(dim1path,'waypoints.txt')
            with open(epath,"w")as e:
                for k in waypointe:
                    e.write(k)