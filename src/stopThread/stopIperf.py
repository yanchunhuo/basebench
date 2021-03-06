#!-*- coding:utf8 -*-
from src.common.fileTool import FileTool
from src.pojo.Compute import Compute
from src.testStability.testIperf import TestIperf
import threading

class StopIperf(threading.Thread):
    def __init__(self,accountResourceFilePath):
        threading.Thread.__init__(self,name='stopIperf')
        self._accountResourceFilePath=accountResourceFilePath

    def run(self):
        testIperf = TestIperf()
        iperfAccountResource=FileTool.readJsonFromFile(self._accountResourceFilePath)
        compute_pair_array=iperfAccountResource['_iperfComputePairs']
        for compute_pair in compute_pair_array:
            compute_client=Compute()
            compute_server=Compute()
            compute_client.__dict__ = compute_pair[0]
            compute_server.__dict__ = compute_pair[1]
            testIperf.stop(compute_client,compute_server)