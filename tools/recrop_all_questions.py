"""
coolChem - Precision Question Recropping Tool
=============================================
Re-crops all Section A past paper question images from the original
Question Paper PDFs with exact bounding boxes, ensuring every question
prompt, context stem, and answer lines are 100% visible and accurate.
"""

import os
import re
import json
import fitz  # PyMuPDF
from PIL import Image
import io

REPO_DIR = r"C:\Users\Alexander\.gemini\antigravity\scratch\coolChem"
QUESTIONS_FILE = os.path.join(REPO_DIR, "questions.json")

PDF_MAP = {
    '2001-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795088948067_041957fd.pdf',
    '2001-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795088947973_c94e2066.pdf',
    '2001-june-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795091648051_8353c2ce.pdf',
    '2001-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795091648088_a99c28dc.pdf',
    '2001-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795091648071_917bd503.pdf',
    '2002-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094005002_623e4808.pdf',
    '2002-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094004834_138c61f3.pdf',
    '2002-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094004875_5e6d4ec6.pdf',
    '2002-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094004507_971a60fb.pdf',
    '2002-june-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094776861_548b4769.pdf',
    '2002-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094776962_62f7850d.pdf',
    '2002-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094776927_35605fd8.pdf',
    '2002-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094776861_6b55f36d.pdf',
    '2002-june-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795094776889_dcdc0dd5.pdf',
    '2003-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463563_9fb5ce0e.pdf',
    '2003-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463338_dbb54824.pdf',
    '2003-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463606_01130d35.pdf',
    '2003-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463604_1e358153.pdf',
    '2003-jan-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795372463561_eebd3925.pdf',
    '2003-june-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023200_d1fdd406.pdf',
    '2003-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023287_2344f672.pdf',
    '2003-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023395_abd178d4.pdf',
    '2003-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023341_0f87e524.pdf',
    '2003-june-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795376023344_5bb64768.pdf',
    '2004-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960711_d83e0ad2.pdf',
    '2004-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960738_8da10bc5.pdf',
    '2004-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960886_d6991030.pdf',
    '2004-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960916_d1c191c7.pdf',
    '2004-jan-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795377960895_e3fc9c52.pdf',
    '2004-june-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921122_4c1e5527.pdf',
    '2004-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921125_fadf2276.pdf',
    '2004-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921127_77aaa068.pdf',
    '2004-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795379921129_89796597.pdf',
    '2004-june-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795381684205_d8d79a05.pdf',
    '2005-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382849471_29d4088b.pdf',
    '2005-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382849428_1c35b8c8.pdf',
    '2005-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382849486_6024c1f3.pdf',
    '2005-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382904753_27df4626.pdf',
    '2005-jan-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382904770_4d77c63a.pdf',
    '2005-jan-chm6w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382904766_6115b880.pdf',
    '2005-june-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382980188_94874931.pdf',
    '2005-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382980221_a694d6cb.pdf',
    '2005-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795382980203_a71451e6.pdf',
    '2005-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003706_b9ecaf08.pdf',
    '2005-june-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003708_7ca682eb.pdf',
    '2005-june-chm6w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383003756_890ad502.pdf',
    '2006-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383041331_c9fa92fd.pdf',
    '2006-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383041323_9dad2176.pdf',
    '2006-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383041347_39b4eb07.pdf',
    '2006-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383041377_6a23cdc0.pdf',
    '2006-june-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383066745_4f369b0a.pdf',
    '2006-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383066798_743f5157.pdf',
    '2006-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383066769_beac6c3b.pdf',
    '2006-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383083064_6e7b7914.pdf',
    '2006-june-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383083059_3d319834.pdf',
    '2006-june-chm6w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795383083058_f1d8cd22.pdf',
    '2007-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795469473805_adb08af9.pdf',
    '2007-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795469473824_f40f348a.pdf',
    '2007-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795469473822_32602c73.pdf',
    '2007-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795469473872_8c753ee3.pdf',
    '2007-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222360_1bff8756.pdf',
    '2007-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222448_63b0d554.pdf',
    '2007-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222468_a1e6a223.pdf',
    '2007-june-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795470222573_c7a4b8b1.pdf',
    '2008-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471418112_dfec1f4a.pdf',
    '2008-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471418121_ead38ac6.pdf',
    '2008-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471418113_220d39bf.pdf',
    '2008-june-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471943592_47db533b.pdf',
    '2008-june-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471943570_80c22de0.pdf',
    '2008-june-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471943585_f4dd83b9.pdf',
    '2008-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471967917_a7f9469a.pdf',
    '2008-june-chm5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471967932_47e2b7fa.pdf',
    '2008-june-chm6w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795471967992_a0217e33.pdf',
    '2009-jan-chm1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472259568_4e901e40.pdf',
    '2009-jan-chm2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472259573_661408ee.pdf',
    '2009-jan-chm3w': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472300683_c1be80ef.pdf',
    '2009-jan-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472300684_080e61c4.pdf',
    '2009-jan-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472326013_11b23d94.pdf',
    '2009-specimen-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472326003_2e90987b.pdf',
    '2009-june-chm4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472598951_fd5640a0.pdf',
    '2010-jan-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472702126_c657240d.pdf',
    '2010-jan-chem2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472702128_9f344afb.pdf',
    '2010-jan-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472712130_6462ffad.pdf',
    '2010-jan-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795472712131_77415ceb.pdf',
    '2010-june-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474010444_9bcb40d8.pdf',
    '2010-june-chem2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474010377_a22b3f7c.pdf',
    '2010-june-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474010809_67b92868.pdf',
    '2010-june-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474010620_b87f33dd.pdf',
    '2011-jan-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474050861_aeb2c338.pdf',
    '2011-jan-chem2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474050855_8104a779.pdf',
    '2011-jan-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474074257_da4a9f6e.pdf',
    '2011-jan-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474074262_c366b1fd.pdf',
    '2011-june-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474239850_2896b5a4.pdf',
    '2011-june-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474293039_800bcf47.pdf',
    '2011-june-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795474293070_c99e1967.pdf',
    '2012-jan-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512340760_5d7d6143.pdf',
    '2012-jan-chem2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512340923_5d0f81dc.pdf',
    '2012-jan-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512363659_b0526e57.pdf',
    '2012-jan-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512363575_04e4191c.pdf',
    '2012-june-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512406270_36a6ba56.pdf',
    '2012-june-chem2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512406290_38e436e6.pdf',
    '2012-june-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512422681_a4173266.pdf',
    '2012-june-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795512422717_7b3eb6ca.pdf',
    '2013-jan-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514228049_19bf85de.pdf',
    '2013-jan-chem2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514228031_c31c9f3c.pdf',
    '2013-jan-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514239841_80c2bbc9.pdf',
    '2013-jan-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514239844_a663c23a.pdf',
    '2013-june-chem1': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514279276_adb4c885.pdf',
    '2013-june-chem2': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514279241_53fd1d27.pdf',
    '2013-june-chem4': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514296144_6badbd7b.pdf',
    '2013-june-chem5': r'C:\Users\Alexander\.gemini\antigravity\brain\8512efd8-03d2-4069-bf73-26ca25b72d40\.user_uploaded\media_1795514296106_2c1f18f2.pdf',
}

def extract_lines(page):
    blocks = page.get_text('dict')['blocks']
    lines = []
    for b in blocks:
        if 'lines' in b:
            for l in b['lines']:
                txt = ''.join([s['text'] for s in l['spans']]).strip()
                bbox = l['bbox']
                if txt and 60 <= bbox[1] <= 814:
                    lines.append((bbox, txt))
    lines.sort(key=lambda x: (x[0][1], x[0][0]))
    return lines

def main():
    print("Loading questions.json...")
    with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
        db = json.load(f)

    # 1. Correct misindexed page numbers if any
    fixed_pages = 0
    for q in db['questions']:
        if q['id'] == '2002-jan-chm1-q3cii' and q.get('page') != 6:
            q['page'] = 6
            fixed_pages += 1
        elif q['id'] == '2002-jan-chm1-q4di' and q.get('page') != 8:
            q['page'] = 8
            fixed_pages += 1
    if fixed_pages > 0:
        print(f"Fixed {fixed_pages} misindexed question page numbers in questions.json")

    # 2. Open documents
    docs = {p: fitz.open(path) for p, path in PDF_MAP.items()}

    # 3. Group questions by (paper, page)
    from collections import defaultdict
    pages = defaultdict(list)
    for q in db['questions']:
        if q['paper'] in docs:
            pages[(q['paper'], q['page'])].append(q)

    total_target = sum(len(ql) for ql in pages.values())
    print(f"Processing {total_target} questions across {len(pages)} pages in {len(docs)} papers...")

    success_count = 0
    total_count = 0

    for (paper, p_num), q_list in sorted(pages.items()):
        doc = docs[paper]
        page = doc[p_num - 1]
        lines = extract_lines(page)

        # Check for main question number at top of page
        main_q_top = None
        for bbox, txt in lines:
            if bbox[0] < 70 and re.match(r'^\d+$', txt.strip()):
                main_q_top = (int(txt.strip()), bbox[1])
                break

        # Check for explicit subpart letter headers on page: (a), (b), (c), etc.
        subpart_letter_locs = []
        for bbox, txt in lines:
            if bbox[0] < 120:
                m_sub = re.match(r'^\(([a-h])\)', txt.strip())
                if m_sub:
                    subpart_letter_locs.append((m_sub.group(1), bbox[1]))

        # Locate label for each question
        curr_y = 60.0
        located = []
        for q_idx, q in enumerate(q_list):
            total_count += 1
            q_label = q['question']
            m = re.match(r'^(\d+)?(?:\(([a-z\d]+)\))?(?:\(([a-z\d]+)\))?', q_label)
            main_q, sub1, sub2 = m.groups() if m else (None, None, None)

            # Bound search by subsequent subpart letter if known
            max_search_y = 800.0
            if sub1:
                for s_char, s_y in subpart_letter_locs:
                    if s_char > sub1 and s_y >= curr_y - 5:
                        max_search_y = min(max_search_y, s_y)
                        break

            # Check if parent subpart (e.g. (b) or 1 (b) before (i)) appears on this page
            parent_sub_y0 = None
            if sub2 and (q_idx == 0 or not q_list[q_idx-1]['question'].startswith(f"{main_q}({sub1})")):
                for bbox, txt in lines:
                    if curr_y - 5 <= bbox[1] < max_search_y and bbox[0] < 120:
                        words = txt.split()
                        if words and (
                            words[0] == f"({sub1})"
                            or (
                                (txt.startswith(f"{main_q} ({sub1})") or txt.startswith(f"{main_q}({sub1})"))
                                and not re.match(rf'^{re.escape(main_q)}\s*\({re.escape(sub1)}\)\s*\(', txt)
                            )
                        ):
                            parent_sub_y0 = bbox[1]
                            break

            candidates = []
            if sub2:
                if main_q and sub1:
                    candidates.append(f"{main_q} ({sub1}) ({sub2})")
                    candidates.append(f"{main_q}({sub1})({sub2})")
                    candidates.append(f"{main_q} ({sub1})({sub2})")
                candidates.append(f"({sub2})")
                if sub1:
                    candidates.append(f"({sub1})({sub2})")
                    candidates.append(f"({sub1}) ({sub2})")
            elif sub1:
                candidates.append(f"({sub1})")
                if main_q:
                    candidates.append(f"{main_q} ({sub1})")
                    candidates.append(f"{main_q}({sub1})")
            elif main_q:
                candidates.append(main_q)

            found_y0 = None
            search_start = parent_sub_y0 if parent_sub_y0 is not None else curr_y
            for bbox, txt in lines:
                if search_start - 5 <= bbox[1] < max_search_y:
                    for cand in candidates:
                        if bbox[0] < 140:
                            words = txt.split()
                            if (words and (words[0] == cand or txt.startswith(cand))) or txt == cand:
                                found_y0 = bbox[1]
                                break
                    if found_y0 is not None:
                        break

            # Fallback for continued question without explicit label on current page
            if found_y0 is None and q_idx == 0 and len(lines) > 0:
                found_y0 = lines[0][0][1]

            actual_y0 = parent_sub_y0 if parent_sub_y0 is not None else found_y0
            located.append((q, found_y0, actual_y0))
            if found_y0 is not None:
                curr_y = found_y0 + 10.0

        # Calculate bounding boxes and crop images
        for i, (q, ly0, start_y0) in enumerate(located):
            if ly0 is None:
                print(f"ERROR: Could not locate label for {q['id']} ({q['question']}) on page {p_num}")
                continue

            # y0 calculation
            if q.get("crop_y0") is not None:
                y0 = float(q["crop_y0"])
            elif i == 0:
                m = re.match(r'^(\d+)', q['question'])
                q_num = int(m.group(1)) if m else None
                if main_q_top and q_num and main_q_top[0] == q_num and main_q_top[1] < start_y0:
                    y0 = max(68.0, main_q_top[1] - 8.0)
                else:
                    y0 = max(68.0, start_y0 - 8.0)
            else:
                y0 = max(68.0, start_y0 - 8.0)

            # y1 calculation
            if i + 1 < len(located) and located[i+1][2] is not None:
                y1 = located[i+1][2] - 6.0
            else:
                # Last question on page: capture down through marks/lines
                max_y_end = 815.0 if paper.startswith('2007-june-') else 785.0
                max_y1 = 815.0 if paper.startswith('2007-june-') else 775.0
                after_lines = [
                    l for l in lines 
                    if l[0][1] >= ly0 and l[0][3] < max_y_end
                    and 'Turn over' not in l[1] 
                    and 'APW/' not in l[1] 
                    and 'Section B' not in l[1]
                    and 'Answer these questions' not in l[1]
                    and not re.match(r'^\d+$', l[1].strip())
                ]
                if after_lines:
                    last_y = max(l[0][3] for l in after_lines)
                    y1 = min(max_y1, last_y + 18.0)
                else:
                    y1 = min(max_y1, ly0 + 120.0)
                if paper.startswith('2007-june-'):
                    notice_y0s = [
                        l[0][1] for l in lines
                        if l[0][1] > ly0 and (
                            'Section B' in l[1]
                            or 'Answer these questions' in l[1]
                            or 'Turn over' in l[1]
                        )
                    ]
                    if notice_y0s:
                        y1 = min(y1, min(notice_y0s) - 3.0)

            # Render high-resolution crop (optionally excluding embedded figure bands)
            exclude_y = sorted(q.get("crop_exclude_y") or [])
            if not exclude_y:
                rect = fitz.Rect(35, y0, 545, y1)
                pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
                im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")
            else:
                strips = []
                cur = y0
                for ey0, ey1 in exclude_y:
                    if ey0 > cur + 2:
                        strips.append((cur, min(ey0, y1)))
                    cur = max(cur, ey1)
                if cur < y1 - 2:
                    strips.append((cur, y1))
                parts = []
                for sy0, sy1 in strips:
                    if sy1 > sy0 + 2:
                        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=fitz.Rect(35, sy0, 545, sy1))
                        parts.append(Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB"))
                if parts:
                    total_h = sum(p_im.height for p_im in parts)
                    im = Image.new("RGB", (parts[0].width, total_h), (255, 255, 255))
                    yy = 0
                    for p_im in parts:
                        im.paste(p_im, (0, yy))
                        yy += p_im.height
                else:
                    rect = fitz.Rect(35, y0, 545, y1)
                    pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0), clip=rect)
                    im = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB")

            # Output path
            img_rel = q["image"]
            img_abs = os.path.join(REPO_DIR, img_rel.replace("/", os.sep))
            os.makedirs(os.path.dirname(img_abs), exist_ok=True)

            im.save(img_abs, format="JPEG", quality=92)
            success_count += 1

    print(f"\nSuccessfully cropped {success_count} / {total_count} questions!")

    # Save updated questions.json
    with open(QUESTIONS_FILE, 'w', encoding='utf-8') as f:
        json.dump(db, f, indent=2, ensure_ascii=False)
    print("Updated questions.json successfully!")

if __name__ == "__main__":
    main()
