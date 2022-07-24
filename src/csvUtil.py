import os
from threading import Thread

import pandas as pd

from config.config import config, getPath
from filter import *
from logger import log

threadList = []
globalThreadList = []
inputfilePath = config.get('inputfilePath')


def chunkReader(inputArr: list, target, chunkSize: int):
    chunkSize = min(chunkSize, config.get('maxChunkSize'))
    size = len(inputArr)
    start = 0
    end = None
    while start < size:
        if size - start <= chunkSize:
            end = size
        else:
            end = start + chunkSize
        t = Thread(target=target, args=[inputArr, start, end])
        t.start()
        globalThreadList.append(t)
        start += chunkSize


def readDept():
    log("Reading department CSV")
    try:
        with open(os.path.join(getPath('inputfilePath'), "departments.csv"), mode='r') as file:
            deptRows = pd.read_csv(file, usecols=[0, 1]).values.tolist()
            chunkReader(deptRows, setDept, 1000)
    except FileNotFoundError:
        log('departments.csv not found', isExit=True, errorCode='fileError')
        raise FileNotFoundError


def readProduct():
    log("Reading Product CSV")
    try:
        with open(os.path.join(getPath('inputfilePath'), "products.csv"), mode='r', encoding="utf8") as file:
            productRows = pd.read_csv(file, usecols=[0, 3]).values.tolist()
            chunkReader(productRows, setProducts, 1000)
    except FileNotFoundError:
        log('products.csv not found', isExit=True, errorCode='fileError')
        raise FileNotFoundError


def readPriorOrder():
    log("Reading Order Prior CSV")
    try:
        with open(os.path.join(getPath('inputfilePath'), "order_products__prior.csv"), mode='r',
                  encoding="utf8") as file:
            orderPriorRows = pd.read_csv(file, usecols=[0, 1]).values.tolist()
            chunkReader(orderPriorRows, setPriorProducts, 50000)
    except FileNotFoundError:
        log('order_products__prior.csv not found', isExit=True, errorCode='fileError')
        raise FileNotFoundError


def readTrainOrder():
    log("Reading Order Train CSV")
    try:
        with open(os.path.join(getPath('inputfilePath'), "order_products__train.csv"), mode='r',
                  encoding="utf8") as file:
            orderTrainRows = pd.read_csv(file, usecols=[0, 1]).values.tolist()
            chunkReader(orderTrainRows, setTrainProducts, 10000)
    except FileNotFoundError:
        log('order_products__train.csv not found', isExit=True, errorCode='fileError')
        raise FileNotFoundError


def readData():
    initializeOutputObject()
    threadList = [Thread(target=readDept), Thread(target=readProduct), Thread(
        target=readPriorOrder), Thread(target=readTrainOrder)]
    for th in threadList:
        th.start()
    for t in threadList:
        t.join()
    for t in globalThreadList:
        t.join()


def processData():
    log("Reading Order CSV")
    try:
        with open(os.path.join(getPath('inputfilePath'), "orders.csv"), mode='r', encoding="utf8") as file:
            orderRows = pd.read_csv(file, usecols=[0, 2, 4, 5]).values.tolist()
            chunkReader(orderRows, setOrder, 30000)
    except:
        log('orders.csv not found', isExit=True, errorCode='fileError')
        raise FileNotFoundError
