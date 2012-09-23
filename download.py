from autodebate import *
         
def downloadObama():
    obama = ObamaCorpus()
    for speech in range(800, 1060):
        url = 'http://projects.washingtonpost.com/obama-speeches/speech/' + str(speech)
        print "Fetching %s" % url
        obama.digestSpeech(url)
        
        f = open('obama', 'w')
        pickle.dump(obama, f)
        f.close()
    
            
def downloadRomney():
    romney = RomneyCorpus()
    urls = [
       'http://mittromneycentral.com/speeches/2012-speeches/072412-remarks-at-the-vfw-national-convention/',
       'http://mittromneycentral.com/speeches/2012-speeches/081412-mitt-romneys-speech-in-chillicothe-ohio/',
       'http://mittromneycentral.com/speeches/2012-speeches/071112-speech-to-the-naacp-convention/',
       'http://mittromneycentral.com/speeches/2012-speeches/072912-mitt-romney-policy-speech-in-jerusalem/',
       'http://mittromneycentral.com/speeches/2012-speeches/062112-remarks-to-naleo-growing-opportunity-for-all-americans-2/',
       'http://mittromneycentral.com/speeches/2012-speeches/052312-remarks-on-education-a-chance-for-every-child-2/',
       'http://mittromneycentral.com/speeches/2012-speeches/041312-nra-convention-2012/',
       'http://mittromneycentral.com/speeches/2012-speeches/051512-prairie-fire-of-debt-speech/',
       'http://mittromneycentral.com/speeches/2012-speeches/051212-liberty-university-commencement-address/',
       'http://mittromneycentral.com/speeches/2012-speeches/040412-newspaper-association-of-america-remarks/',
       'http://mittromneycentral.com/speeches/2012-speeches/040312-wisconsin-victory-speech/',
       'http://mittromneycentral.com/speeches/2012-speeches/033012-freedom-and-opportunity/',
       'http://mittromneycentral.com/speeches/2012-speeches/032012-illinois-victory-speech/',
       'http://mittromneycentral.com/speeches/2012-speeches/031912-remarks-in-chicago-the-freedom-to-dream/',
       'http://mittromneycentral.com/speeches/2012-speeches/030612-super-tuesday/',
       'http://mittromneycentral.com/speeches/2012-speeches/022412-speech-at-the-detroit-economic-club/',
       'http://mittromneycentral.com/speeches/2012-speeches/020412-nevada-caucus-victory-speech/',
       'http://mittromneycentral.com/speeches/2012-speeches/013112-mitt-romneys-florida-primary-victory-speech/',
       'http://mittromneycentral.com/speeches/2012-speeches/011012-mitt-romneys-new-hampshire-primary-victory-speech/',
       'http://mittromneycentral.com/speeches/2011-speeches/120711-remarks-to-the-republican-jewish-coalition/',
       'http://mittromneycentral.com/speeches/2011-speeches/100811-values-voters-summit-2011/',
       'http://mittromneycentral.com/speeches/2011-speeches/10072011-an-american-century/',
       'http://mittromneycentral.com/speeches/2011-speeches/090211-republican-national-hispanic-assembly/',
       'http://mittromneycentral.com/speeches/2011-speeches/083011-vfw-national-convention/',
       'http://mittromneycentral.com/speeches/2011-speeches/060211-mitt-romney-announces-his-2012-run-for-president/',
    ]
    for url in urls:
        print "Fetching %s" % url
        romney.digestSpeech(url)

    f = open('romney', 'w')
    pickle.dump(romney, f)
    f.close()

downloadRomney()
#downloadObama()