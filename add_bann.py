#!/usr/bin/python
# -*- coding: utf-8 -*-
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path, PureWindowsPath
import img2pdf, os

dirnamePureWin = Path("C:\\palashworld\\_docs\\IDS\\1\\")
dirFontPureWin= Path ("C:\\Users\\polta.work\\AppData\\Local\\Microsoft\\Windows\\Fonts\\")
outFilePDF = os.path.join(dirnamePureWin, u"subaru_foreter_2010.pdf")
fontPathBN = os.path.join(dirFontPureWin,"Lipi-Padmo-Unicode.ttf")

imgFullListSrc = []
imgFullListMrkd = []
for fname in os.listdir(dirnamePureWin):
	if fname.endswith(".jpg"):
		path = os.path.join(dirnamePureWin, fname)
		# if os.path.isdir(path):
			# continue
		imgFullListSrc.append(path)
	
for imageLi in imgFullListSrc:
	inputImage = Image.open(imageLi).convert('RGBA')
	image2Watermark = Image.new('RGBA',inputImage.size,  (255, 255, 255, 0))
	draw = ImageDraw.Draw(image2Watermark)
	width, height = inputImage.size
	margin = 10
	font = ImageFont.truetype(fontPathBN, int(height / 30))
	finalWaterText= u"পরিচয় নথি -লস্কর"
	
	finalWaterText= ""
	textWidth, textHeight = draw.textsize(finalWaterText, font)
	x = width - textWidth - margin
	y = height - textHeight - margin
	draw.text((1100, 1300), finalWaterText, "black", font)
	watermarked_image= Image.alpha_composite(inputImage, image2Watermark)
	watermarked_image = watermarked_image.convert('RGB')
	outFile = imageLi.replace(".", "_Mrkd.")
	print('\n outFile = ',outFile)
	watermarked_image.save(outFile)
	imgFullListMrkd.append(outFile)

with open(outFilePDF,"wb") as f:
	f.write(img2pdf.convert(imgFullListMrkd)) 