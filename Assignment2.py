import urllib


def downloadData(url):
    content = urllib.request.urlopen(url).read().decode()
    return content


dataFile = {}


def stringIO(file):
    pass


def processData(file):
    data = StringIO(file)
    csv_reader = csv.reader(data, delimiter=',')
    next(csv_reader)

    index = 2
    for lines in csv_reader:
        try:
            birthday = datetime.datetime.strptime(lines[2], '%d/%m/%y').date()
        except:
            logger.error("error processing line{} for id {}".format(index, lines[0]))
        finally:
            index += 1


def displayPerson(id, personData=None):
    if personData is None:
        personData = dataFile
    if id in personData.keys():
        print("Person {} is {} with a birthdate of {}".format(id, personData[id][0], personData[id][1]))

    else:
        print("No person found with that id number")


def main():
    global logger, csvData
    logger = logging.getLogger('assignment 2')
    fh = logging.FileHandler('error.log')
    fh.setLevel(logging.ERROR)
    logger.addHandler(fh)

    commandParser = argparse.ArgumentPareser(description="Send a url parameter to the script")

    commandParser.add_argument("--url", type=str, help="Link to the CSV")

    args = commandParser.parse_args()

    if not args.url:
        exit()

    try:
        csvData = downloadData(args.url)
    except:
        print("An error has occurred. Try again.")
        exit()

    processData(csvData)

    isTrue = True
    while isTrue:
        x = input("Enter ID: ")
        if int(x) > 0:
            displayPerson(x)
        else:
            isTrue = False

    if __name__ == "__Assignment2__":
        main()
