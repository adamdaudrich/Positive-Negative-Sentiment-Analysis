input_file = open('assets/project_twitter_data.csv','r')
output_file = open('assets/resulting_data.csv','w')

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#strip tweets of punctuation

def strip_punctuation(tweet_text):
    cl_tweet = tweet_text
    for char in punctuation_chars:
        cl_tweet = cl_tweet.replace(char,'')
        
    return cl_tweet


# positive word count function

positive_words = []
with open("assets/positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(tweet_text):
    tweet_lwr = strip_punctuation(tweet_text.lower())
    pos_count = 0
    for word in tweet_lwr.split():
        if word in positive_words:
            pos_count += 1
        else:
            continue
    return pos_count 


#negative word count function

negative_words = []
with open("assets/negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_neg(tweet_text):
    cl_tweet_lwr = strip_punctuation(tweet_text.lower())
    neg_count = 0
    for word in cl_tweet_lwr.split():
        if word in negative_words:
            neg_count += 1
        else:
            continue
    return neg_count

# write headers to the output file
output_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')

# skip over the header before starting the input loop
input_file.readline()

# INPUT LOOP
# step 1/4 : clean each twitter line of punctuation

for line in input_file:
    row = line.strip().split(',')

# step 2/4: creation of variables: extract tweet_text, retweet_count, reply_count
    tweet_text = row[0]
    retweet_count = row[1]
    reply_count = row[2]
    
# step 3/4: calculate positive, negative, net scores
    pos_score = get_pos(tweet_text)
    neg_score = get_neg(tweet_text)   
    net_score = pos_score - neg_score
    
# step 4/4: write the results to the output file
    row_string = '{},{},{},{},{}'.format(retweet_count, reply_count, pos_score, neg_score, net_score)
    output_file.write(row_string)
    output_file.write('\n')

input_file.close()
output_file.close()
