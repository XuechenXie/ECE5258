myFolder = './test_og';
filePattern = fullfile(myFolder, '*.jpg');
jpegFiles = dir(filePattern);
length(jpegFiles)
for k = 1:length(jpegFiles)
    baseFileName = jpegFiles(k).name;
    fullFileName = fullfile(myFolder, baseFileName);
    fprintf(1, 'Now reading %s\n', fullFileName);
    img = imread(fullFileName);
    
%     if size(img,3)==3
     RGB = locallapfilt(img,0.4,0.5);
%     else
        
%     end
    fullFileName = fullfile('./test_laplacian', baseFileName);
    imwrite(RGB, fullFileName);
end