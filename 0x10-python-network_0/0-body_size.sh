#!/bin/bash
#Get the byte size of a Http response header of a given url
curl -s "$1" | wc -c
