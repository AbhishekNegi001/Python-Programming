# interactive debugging
import pdb
def seq(n):
    for i in range(n):
        pdb.set_trace() #breakpoint
        print(i)
    return

seq(5)

# c : continue
# q : quit
# h : help
# list
# p: print
# p locals()
# p globals()
