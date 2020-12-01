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
        HSV = rgb2hsv(img);
        Heq = histeq(HSV(:,:,3));
        HSVmod = HSV;
        HSVmod(:,:,3) = Heq;
        RGB = hsv2rgb(HSVmod);
    else
        RGB = histeq(img);
    end
    
    
    fullFileName = fullfile('./train_HE', baseFileName);
    imwrite(RGB, fullFileName);
end