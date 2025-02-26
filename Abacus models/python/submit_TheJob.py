
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
from abaqus import *
import job
import sys
def Submit_the_job(model_1_name, Delamination_case = 4):


    jobname = mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='{}-{}'.format(model_1_name, Delamination_case), modelPrint=
        OFF, multiprocessingMode=DEFAULT, name='Job-{}'.format(Delamination_case), nodalOutputPrecision=SINGLE
        , numCpus=2, numDomains=2, numGPUs=2, numThreadsPerMpiProcess=1, queue=None
        , resultsFormat=ODB, scratch='', type=ANALYSIS, userSubroutine='', 
        waitHours=0, waitMinutes=0)
    mdb.jobs['Job-{}'.format(Delamination_case)].submit(consistencyChecking=OFF)