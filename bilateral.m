myFolder = './train';
filePattern = fullfile(myFolder, '*.jpg');
jpegFiles = dir(filePattern);
length(jpegFiles)
for k = 1:length(jpegFiles)
    baseFileName = jpegFiles(k).name;
    fullFileName = fullfile(myFolder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    img = imread(fullFileName);
    if size(img,3)==3
        LAB = rgb2lab(img);
        patch = imcrop(LAB,[170,35,50,50]);
        patchSq = patch.^2;
        edist = sqrt(sum(patchSq,3));
        patchVar = std2(edist).^2;
        if patchVar <= 0
            patchVar = 1;
        end
        LAB1 = imbilatfilt(LAB,2*patchVar,2);
        B1 = lab2rgb(LAB1,'Out','uint8');
    else
        patch = imcrop(img,[170,35,50,50]);
        patchVar = std2(patch)^2;
        if patchVar <= 0
            patchVar = 1;
        end
        B1 = imbilatfilt(img,2*patchVar,2);
    end
    fullFileName = fullfile('./train_bila', baseFileName);
    imwrite(B1, fullFileName);
end