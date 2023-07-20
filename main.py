import collector.core as collect
from helpers.loader import Loader 


print("---------------------------------------------------------------- ")
print("---------------------------------------------------------------- ")
print("   This is a simple example of how to use the Github repositories")
print("   collector. The collector is based on the Github API and it ")
print("   allows to search for repositories and files in the repositories")
print("   using keywords. ")
print("---------------------------------------------------------------- ")
print("---------------------------------------------------------------- ")
print("\n")
    
if __name__ == "__main__":
    loader = Loader("Collecting Github repositories...", "\nFinish!", 0.05).start()
    result = collect.search_in_code('keras.layers.convolutional')
    loader.stop()
print("---------------------------------------------------------------- ")