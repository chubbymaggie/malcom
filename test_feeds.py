from Malcom.feeds.feed import FeedEngine
import os

all_feeds = [
			"AsproxTracker",
			"CybercrimeTracker",
			"FeodoTracker",
			"MalcodeBinaries",
			"MalwaredRu",
			"MalwareTrafficAnalysis",
			"MalwareDomainList",
			"PalevoTracker",
			"TorExitNodes",
			"ZeusTrackerBinaries",
			"ZeusTrackerConfigs",
			"ZeusTrackerDropzones",
			 ]

feed_dir = os.getcwd()+'/Malcom/feeds'
print "Testing feeds in", feed_dir
fe = FeedEngine({'FEEDS_DIR': feed_dir})

fe.load_feeds([f.lower() for f in all_feeds])

results = {}

for feed in fe.feeds:
	print "Testing feed %s" % feed
	fe.feeds[feed].testing = True
	fe.feeds[feed].update()
	print "Test on %s succeeeded (%s elements fetched)" % (feed, fe.feeds[feed].elements_fetched)
	results[feed] = fe.feeds[feed].elements_fetched

print "Test results:"
for f in results:
	print "{0: <32} {1:8}".format(f, results[f])




