from textblob import  TextBlob

Text="python is my favourite programming language"
obj=TextBlob(Text)
Sentiment=obj.sentiment.polarity
print(Sentiment)

