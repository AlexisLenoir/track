import os
import sys
import benchTrack.tools as tl
import benchTrack.structureBench as bt

def manage_flag(argv,bench):
    """

    This function manage all flags,
    with a flag for show a list or the information,this function call a function to show that
    with a flag include or exclude,this function change the object bench
    without flag,return 1

    :param argv:args Bench:l'object benchTrack

    """
    for i in range(len(argv)):
        if "--target-include" == argv[i]:
            tl.flagTargets(argv[i:],bench,"include")
        if "--target-exclude" == argv[i]:
            tl.flagTargets(argv,bench,"exclude")
        if "--target-list" == argv[i]:
            tl.flagTargets(argv[i:],bench,"list")
            return 0
        if "--target-info" == argv[i]:
            tl.flagTargets(argv[i:],bench,"info")
            return 0

        if "--task-include" == argv[i]:
            tl.flagTasks(argv[i:],bench,"include")
        if "--task-exclude" == argv[i]:
            tl.flagTasks(argv[i:],bench,"exclude")
        if "--task-liste" == argv[i]:
            tl.flagTasks(argv[i:],bench,"list")
            return 0
        if "--task-info" == argv[i]:
            tl.flagTasks(argv[i:],bench,"info")
            return 0
    return 1

def exe(argv):
    """
    execution of the tool BenchTrack

    :param str argv: input in the terminal.

    """
    if len(argv) < 2:
        print("Missing parameter")
        return -1
    path_benchTrack = os.path.dirname(os.path.dirname(os.path.abspath( __file__ )))
    bench = bt.BenchTrack(argv[-1], path_benchTrack)
    if manage_flag(argv,bench):
        bench.exe_bench()
        bench.ToCsv()
if __name__ == '__main__':
    exe(sys.argv)
