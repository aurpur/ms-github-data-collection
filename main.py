import collector.core as collect 


print("---------------------------------------------------------------- ")
print("---------------------------------------------------------------- ")
print("   This is a simple example of how to use the Github repositories")
print("   collector. The collector is based on the Github API and it ")
print("   allows to search for repositories and files in the repositories")
print("   using keywords. ")
print("---------------------------------------------------------------- ")
print("---------------------------------------------------------------- ")
print("\n")

print(" Collecting Github repositories ...")
result = collect.search_in_code('keras.layers.convolutional')

print("---------------------------------------------------------------- ")