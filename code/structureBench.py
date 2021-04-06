from tools import *
from theme import Theme
#class BenchTrack
class BenchTrack:
    def __init__(self,path_inf):
        self.__path = path_inf
        self.__name = path_inf.split('/')[-1]
        #dictionaire of targets,<key = nameTarget> = objetTarget
        self.__dictTargets={}
        #list of
        self.__listThemes=[]
        self.__allTarget=[]
        self.__allTask = []
        if not self.__construct():
            print("Error:Construct")
        print(self.__str__())
        self.__outputFile = self.__path+"/output.csv"
    def __str__(self):
        string = self.getName()
        string += ":list Themes["
        if len(self.__listThemes) != 0:
            string += self.__listThemes[0].__str__()
        for i in range(1,len(self.__listThemes)):
            string += "," + self.__listThemes[i].__str__()
        string += "]"
        return string

    def __construct(self):
        """
        construct all theme,target,task
        """
        path = self.__path
        
        if not os.path.exists(path):
            print("Error:Test name")
            return 0
        path += self.__name
        #for every theme in the folder test
        path += '/tasks'

        #construt list of targets
        path = self.__path+"/targets"
        for targetName in os.listdir(path):
            self.__allTarget.append(targetName)
        path = self.__path+'/tasks'
        for themeName in os.listdir(path):
            theme = Theme(themeName)
            #for every task in the folder theme
            pathT = path + '/' + themeName
            for taskName in os.listdir(pathT):
                #set in the list alltask
                if taskName not in self.__allTask:
                    self.__allTask.append(taskName)
                pathTs = pathT+'/'+taskName +'/'
                path_config = pathTs + 'config.ini'
                #resd config.ini and construct task
                sample_size = 20
                args = ''
                if os.path.exists(path_config):
                    sample_size,args = ConfigFileTask(path_config)
                task = Task(taskName,args.split(' '),sample_size)
                # set all target
                for targetName in self.__allTarget:
                    # path_target = pathTs + targetName+".py"
                    if existFile(targetName,pathTs):
                        task.addTarget(targetName)
                        
                theme.addTask(task)

            self.__listThemes.append(theme)
            return True
    def getName(self):
        return self.__name

    def ToCsv(self):
        with open(self.__outputFile, "w",newline="") as csvfile:
            writer = csv.writer(csvfile)
            # name of columns
            writer.writerow(["theme", "task", "target", "run_time"])
            # values of columns
            for theme in self.__listThemes:
                theme.ToCsv(writer)

    def addTargets(self,name_target,lang_target):
        self.__dictTargets[name_target] = lang_target

    def __addThemes(self,theme):
        self.__listThemes.append(theme)

    # execution of bench
    def exe_bench(self):
        print("Execution de "+self.__name)
        for i in range(len(self.__listThemes)):
            self.__listThemes[i].exe_theme(self.__allTask,self.__allTarget,self.__name,self.__path)

    def filter_target(self,lis,model):
        if model:
            self.__allTarget = lis
            # print(self.__allTarget)
        else:
            self.__allTarget = [x for x in self.__allTarget if x not in lis]
            # print('List:')
            # print(self.__allTarget)

    def filter_task(self,lis,model):
        if model:
            self.__allTask = lis
            print(self.__allTask)
        else:
            self.__allTask = [x for x in self.__allTask if x not in lis]
            print(self.__allTask)

    def show_list_target(self):
        print("List of targets:")
        for i in range(len(self.__allTarget)):
            print(self.__allTarget[i])

    def showInfoTarget(self,nomTarget):
        print("Information of " + nomTarget + " in the test " + self.__name +":")
        file_read(self.__path+self.__name,nomTarget,"targets")

    def showListTasks(self):
        print("List of tasks:")
        for i in range(len(self.__listThemes)):
            self.__listThemes[i].showlistTasks()

    def showInfoTask(self,nameTask):
        for i in self.__listThemes:
            if i.showInfoTask(nameTask,self.__name,self.__path):
                return 1
        print("Task "+nameTask+" doesn't exite")
        return -1
