# 두 얼굴을 비교하여 얼굴 유사도를 출력!!
# Amazon Rekognition -> Compare Faces
import boto3
def compare_faces(sourceFile, targetFile):
    client = boto3.client('rekognition')
    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=0,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})
    
    for faceMatch in response['FaceMatches']:
        similarity = faceMatch['Similarity']
        
    imageSource.close()
    imageTarget.close()
    return f"두 얼굴의 일치율 : {similarity:.2f}%"