from django.http import HttpResponse
from django.shortcuts import render
# import pytube.request
from .forms import MyForm
from pytube import YouTube
import pytube



def getVideoTitle(yt):
    
    title = yt.title

    return title

def getVideoThumbnail(yt):
    thumbnailURL = yt.thumbnail_url

    return thumbnailURL

def getFileSize(rqst, ytURL):
    fileSizeInBytes = pytube.request.filesize(ytURL)
    fileSize = 0
    if fileSizeInBytes < 10000 :
        fileSize = fileSizeInBytes / 1000
    else: 
        fileSize = fileSizeInBytes / (1000 * 1000)

    return fileSize
    

def getYtURL(request):
    if request.method == 'POST':
        form = MyForm(request.POST)

        if form.is_valid():
            ytURL = form.cleaned_data['url']
            ytRes = form.cleaned_data['res']

            yt = YouTube(ytURL)
            # rqst = pytube.request.filesize(ytURL)

            print(ytRes)
         
            print (f"{ytURL}")
            
            # FILTER
            stream = yt.streams.filter(progressive=True, res=ytRes).first()
            print(stream)
            print("File Size: " + str(stream.filesize_mb) + "MB")
            # print (*yt.streams.filter(progressive=True), sep="\n")
            
            # FILE SIZE 
            # fileSize = getFileSize(rqst, ytURL)
            title = getVideoTitle(yt)
            thumbnail_URL = getVideoThumbnail(yt)

            

            return render(request, "download.html", {"ytURL":ytURL, "title":title, "thumbnail_URL": thumbnail_URL})
    else:
        form = MyForm()
    return render(request, 'index.html', {"form":form})

def download_confirm(request):
    if request.method == "POST":
        ytURL = request.POST.get('ytURL')
        ytRes = request.POST.get('ytRes')

        yt = YouTube(ytURL)
        stream = yt.streams.filter(progressive=True, res=ytRes).first()
        video_path = stream.download()

        return HttpResponse("Download Successfully")
    
    else:
        return HttpResponse("Inavlid request method")
    
def sample_download(request):


    return render(request, 'Document.html')