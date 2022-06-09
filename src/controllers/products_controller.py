#!/usr/bin/env python
# _*_ coding: utf8 _*_

import requests
from Wappalyzer import WebPage, Wappalyzer
import dns.resolver

from pickle import TRUE
from typing import List
from flask import Flask, jsonify, Response
from flask.json import jsonify
from flask_cors import CORS
from werkzeug.wrappers import response


app = Flask(__name__)
CORS(app)

resp = {
    "msg": "Hello World",
    "ok": True,
    "data": []
}


def getProductsExample_CT():
    resp["msg"] = "Productos obtenidos"
    resp["ok"] = True

    return jsonify(resp)


def postProduct_CT(body):
    try:
        reqRow = {"url_target": body["url_target"]}

        url = requests.get(reqRow["url_target"])
        cabeceras = dict(url.headers)
        for x in cabeceras:
            print(x + ": " + cabeceras[x])

        resp["ok"] = True
        resp["msg"] = "Elemento creado"
        resp["data"] = cabeceras

        return jsonify(resp)

    except:
        resp["msg"] = "Error al obtener los Products"
        resp["ok"] = False
        resp["data"] = []

        return jsonify(resp), 500


def wappalizer(body):
    try:
        reqRow = {"url_target": body["url_target"]}

        wap = Wappalyzer.latest()
        web = WebPage.new_from_url(reqRow["url_target"])
        tec = wap.analyze(web)
        tecnologias = list(tec)

        resp["ok"] = True
        resp["msg"] = "Elemento creado"
        resp["data"] = {"tecnologias": tecnologias}

        return jsonify(resp)

    except:
        resp["msg"] = "Error al obtener los Products"
        resp["ok"] = False
        resp["data"] = []

        return jsonify(resp), 500


def obtendns(body):
    try:
        arreglo = []

        answers = dns.resolver.query(body["url_target"], "MX")
        for rdata in answers:
            arreglo.append('%s %s' % (rdata.exchange, rdata.preference))

        resp["ok"] = True
        resp["msg"] = "Elemento creado"
        resp["data"] = {"DNSs": arreglo}

        return jsonify(resp)

    except:
        resp["msg"] = "Error al obtener los Products"
        resp["ok"] = False
        resp["data"] = []

        return jsonify(resp), 500
