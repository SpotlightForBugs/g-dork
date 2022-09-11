from googlesearch import search   #the googlesearch module 
import tldextract                 #extract several information from web addresses
import  argparse                  #the argument parser 


#PARSER START
parser = argparse.ArgumentParser()
only_one = parser.add_mutually_exclusive_group()

parser.add_argument("-q","-query",required="true",help="what you want to find",action="store",dest="target")
only_one.add_argument("-html","-webversion",help="outputs the result as HTML5",action="store_true",dest="html")
only_one.add_argument("-j","-json",help="outputs the result as JSON",action="store_true",dest="json")
only_one.add_argument("-t","-txt",help="outputs the result as a text",action="store_true",dest="text")
parser.add_argument("-qty","-quantity",help="how many results shoud be processed, defaults to 10 results",action='store',default=10,dest='qty',type=int,)
parser.add_argument("-d","-delay",help="how long to wait between searches in seconds, defaults to 1",action='store',default=1,dest='delay',type=int)

args= parser.parse_args()
#PARSER END

#THE PARSED VALUES
query = args.target #what you want to find
num = args.qty      #number of results --> Defaults to 10 
delay = args.delay  #delay between searches in seconds --> Defaults to 1

#END OF PARSED VALUES

#LISTS
links = []
domain_name = []
#END OF LISTS


def search_func():
    '''
    This function searches for the query on google and appends the links to a list.
    :return: A list of links.
    '''
    for j in search(query, tld="com", num=10, stop=num, pause=delay): 
        links.append(j)
        name=(tldextract.extract(j))
        domain_name.append(name.domain+"."+name.suffix)
    


def write_to_file_func():
    '''
    Writes the results to an html file.
    :return: None
    '''
    f = open("results_"+query+".html", "a")
    f.write("<link rel='stylesheet' href='style.css'>")
    f.write('<meta name="viewport" content="width=device-width, initial-scale=1">')
    for item,path in zip (links,domain_name):
        f.write("\n <a class='button'href="+item+">"+path+"</a> <br>")
        f.write("<div class='spacer'</div>")
    

    f.close()


search_func()

if args.html:
    write_to_file_func()
elif args.json:
    print(links)
elif args.text:
    for line in links:
        print (line)


