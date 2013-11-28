#!/usr/bin/python

import re

import tdag
from tdag import rdfGraph, Namespace, RDF, tdag, conflate, process_template, prettyName
from tdag import simUI_d, get_distances, to_nex, draw_graphs, full_grid, process_templates, draw_components

import os
dir = os.path.dirname(__file__)

rdfTemplates = rdfGraph()

instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.load("./template.rdf")

# Get template IDs from RDF
templatesGenerator = rdfTemplates.subjects(RDF.type, instanceNS['desmeme'])

templates = []
for template in templatesGenerator:
	templates.append(template)
			
gTemplates = process_templates(templates, rdfTemplates)

procTemps = { }
for tgraph in gTemplates:

	name = tgraph.name
	g = tgraph.core
	edges = g.edges()

	predToEdge = { }
	for edge in edges:
		edge_props =  g.get_edge_properties(edge)
		pred = edge_props['label']
		n1, n2 = (edge)
		
		if n1 == 'order' or n1 == 'length':
			
			countMatch = re.compile('COUNT(\d)-(\d)')
			matches = countMatch.match(n2)

			if matches: predToEdge[str(pred)] = (matches.group(1))
			else: predToEdge[str(pred)] = (n2)
		
		elif pred != 'COUNT' :
			predToEdge[str(pred)] = (n2)
		
		else: pass # Ignore component counts
		
	procTemps[name] = predToEdge


outfile = open("EntropyTables.txt", "w")

print >> outfile, "name,violability,conditioning,exceptionality,reparability,foundation,stricture,relations,constituent,count"
for tempName in procTemps.keys():
	
	temp = procTemps[tempName]
	
	viol = temp['VIOLABILITY']
	cond = temp['CONDITIONING']
	found = temp['FOUNDATION']
	stric = temp['STRICTURE']
	count = temp['COUNT']
	const = temp['CONSTITUENT']

	try: rel = temp['RELATIONS']
	except: rel = "NA"
	
	try: exc = temp['EXCEPTIONALITY']
	except: exc = "NA"
	
	try: rep = temp['REPARABILITY']
	except: rep = "NA"
		
	print >> outfile, tempName+","+viol+","+cond+","+exc+","+rep+","+found+","+stric+","+rel+","+const+","+count
	

variables = ["violability","conditioning","exceptionality","reparability","foundation","stricture","relations","constituent","count"]



rfile = open("EntropyCalcs.r", "w")

print >> rfile, "library(vcd)"
print >> rfile, "library(entropy)"
print >> rfile, "library(parmigene)"
print >> rfile, ""
print >> rfile,  "templates = read.csv(\'"+dir+"/EntropyTables.txt\', header=TRUE, row.names=1)"
print >> rfile,  ""

for variable in variables:
	print >> rfile,  variable+" = table(templates$"+variable+")"
	print >> rfile,  "names(dimnames("+variable+")) <- list(\'"+variable+"\')";
	print >> rfile,  "H"+variable+" = entropy("+variable+")"
	print >> rfile,  ""

seenpairs = [ ]
for variable1 in variables:

	for variable2 in variables:

		mergedName = variable1+variable2
		reverseMergedName = variable2+variable1
		
		if variable1 == variable2:
			print >> rfile,  mergedName+"MI = 0"
			print >> rfile,  ""
		
		elif reverseMergedName not in seenpairs:
			mergedName = variable1+variable2
			print >> rfile,  mergedName+" = table(templates$"+variable1+",templates$"+variable2+")"
			print >> rfile,  "names(dimnames("+mergedName+")) <- list(\'"+variable1+"\',\'"+variable2+"\')"
			print >> rfile,  mergedName+"MI = mi.shrink("+mergedName+")"
			print >> rfile,  ""
			seenpairs.append(mergedName)
			
		else:
			print >> rfile,  mergedName+" = "+reverseMergedName
			print >> rfile,  mergedName+"MI = "+reverseMergedName+"MI"
			print >> rfile,  ""
			
	print >> rfile,  ""

for variable1 in variables:

	for variable2 in variables:
		
		mergedName = variable1+variable2
		reverseMergedName = variable2+variable1

		print >> rfile,  "P"+mergedName+" = "+mergedName+"MI[1] / H"+variable1 
		print >> rfile,  "P"+reverseMergedName+" = "+mergedName+"MI[1] / H"+variable2 
		print >> rfile,  ""


miRows = [ ]
for variable1 in variables:

	miRow = [ ]
	for variable2 in variables:

		mergedName = variable1+variable2
		miRow.append(mergedName)
		
	miRows.append(miRow)

for miRow, variable in zip(miRows,variables):
	print >> rfile,  variable+"Row = "+"c("+"MI, ".join(miRow)+"MI)"

print >> rfile,  ""
print >> rfile,  "miTemplates = rbind("+"Row, ".join(variables)+"Row)"
print >> rfile,  "colnames(miTemplates) = c(\""+"Col\", \"".join(variables)+"Col\")"

print >> rfile,  ""
print >> rfile,  "miReduced = aracne.a(miTemplates, .05)"

print >> rfile,  ""
print >> rfile,  "mosaic(countreparability, shade=TRUE)"
print >> rfile,  "assoc(countreparability, shade=TRUE)"