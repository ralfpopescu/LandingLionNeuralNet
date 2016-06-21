from NeuralNetUtil import buildExamplesFromLandingLionData
from NeuralNet import buildNeuralNet
import cPickle
from math import pow, sqrt


if  __name__ =='__main__':
    buildNeuralNet(examples, alpha=0.1, weightChangeThreshold = 0.00008,hiddenLayerList = [1], maxItr = sys.maxint, startNNet = None)