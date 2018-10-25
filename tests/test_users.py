import unittest

from flask import Flask, json, request

from run import app

from apie.models.model import Product, Sale, Admin, StoreAttendant


def setUp(self):
        self.client = app.test_client()
        self.User = {
            'username': "Racheal",
            'password': "rac@1234"
        }


