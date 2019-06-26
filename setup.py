from setuptools import setup

setup(
	name='Twitter Sentiment Analysis',
	version='1.0.0',

	description='This script allows to mine twitter data and examine the sentiment of each tweet',

	url='https://github.com/beginnerbunny/Twitter-Sentiment-Analysis/master/setup.py',

	author='Shubhrit Jain',
	author_email='shubhritjain@gmail.com',

	install_requires=['tweepy', 'textblob', 'matplotlib']

	)