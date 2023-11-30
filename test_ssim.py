from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import av
import imageio

def calculate_ssim(img1, img2):
    # Converte le immagini in scala di grigi se necessario
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # Calcola l'indice SSIM
    index, diff = ssim(img1, img2, full=True)
    return index, diff


# Read the 'before' and 'after' images

before = imageio.imread('./dataset/ArtGallery2/Frame_000.png')
after = imageio.imread('.\decompressione_test\ArtGallery2\FLV1\Frame_0.png')

oracle = [0.9519185823219333, 0.9643032466514934, 0.9652946318075225, 0.9639661819335235, 0.9624107101017958, 0.9610554240494354, 0.9594493785269912, 0.9584668587654062, 0.9571737375869153, 0.955963190514788, 0.954516257160479, 0.9531368659078217, 0.9090779505899892, 0.9123888250770309, 0.9124318030036299, 0.9124345871292173, 0.9121080139297764, 0.9118937187326801, 0.9112854186191247, 0.9111858523260545, 0.9112289977451961, 0.9110339767908018, 0.9110290101641229, 0.9104754136710886, 0.9059407815583373, 0.9087094196629804, 0.9088012211886989, 0.9085034971073255, 0.908735529354997, 0.9086766092866584, 0.9083252412812004, 0.9080469431920413, 0.9078628867448688, 0.907591823958583, 0.9074783043182773, 0.9072829446524185, 0.90471042882166, 0.907919477508151, 0.9080253439157556, 0.9079338657450032, 0.9080217344690558, 0.9077698924346537, 0.9079485260822268, 0.9077753790965245, 0.9074169728583935, 0.9070206717360297, 0.907101562895635, 0.9070021220246823, 0.9060889139408239, 0.908966340314241, 0.9089878953382978, 0.908786806089772, 0.9087644496124161, 0.908565145083298, 0.9083515567495128, 0.9083636915415538, 0.9082238222765873, 0.9078010324057931, 0.9075360182154358, 0.9071846957419815, 0.9046933738608431, 0.9081423611530737, 0.9081452236557767, 0.9081755415867422, 0.9083033827310095, 0.9080777919935635, 0.9080916006642046, 0.9078885237316353, 0.9076869513568114, 0.9076999589061483, 0.9075778335182809, 0.9073159275229058, 0.905158752322516, 0.9091483123637173, 0.909383722875484, 0.9091088093710401, 0.9092930517889597, 0.9089722877517771, 0.9091592815683587, 0.9089495465277033, 0.908770616544736, 0.908604976646375, 0.9085325057929664, 0.9084516035728298, 0.9063683709352275, 0.910080163150052, 0.9099622532333371, 0.9100612202626498, 0.9098077240069987, 0.9094379326658214, 0.9093368820708752, 0.9093162206916404, 0.9091076593425594, 0.9091652973061108, 0.9089623966623844, 0.9088288742300015, 0.9050549601295202, 0.9090344733585847, 0.9090945505257502, 0.9088569939644745, 0.9087324872112876]
# Directory contenente le immagini
image_dir = './dataset/ArtGallery2/'

# Lista per memorizzare gli score SSIM calcolati
ssim_scores = []

# Confronta ogni immagine con la successiva
for i in range(0, 101):
    img1_path = f"./dataset/ArtGallery2/Frame_{i:03d}.png"
    print(img1_path)
    img2_path = f".\decompressione_test\ArtGallery2\FLV1\Frame_{i}.png"
    print(img2_path)

    img1 = imageio.imread(img1_path)
    img2= imageio.imread(img2_path)

    # Calcola l'indice SSIM tra due immagini
    ssim_score, _ = calculate_ssim(img1, img2)
    ssim_scores.append(ssim_score)


# Confronta gli score con l'oracolo
for i, (score, oracle_score) in enumerate(zip(ssim_scores, oracle), start=0):
    print(f"Frame {i}: SSIM Score: {score}, Oracle Score: {oracle_score}")

# Compute SSIM between two images with a specified win_size
score, diff = calculate_ssim(before, after)
print(score)

# Convert the difference image to the range [0, 255]
diff = (diff * 255).astype("uint8")

# Threshold the difference image
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Find contours in the thresholded difference image
contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

# Initialize images for visualization
mask = np.zeros(before.shape, dtype='uint8')
filled_after = after.copy()

# Draw rectangles around differing regions and create a mask
for c in contours:
    area = cv2.contourArea(c)
    if area > 40:
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
        cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)
        cv2.drawContours(mask, [c], 0, (0, 255, 0), -1)
        cv2.drawContours(filled_after, [c], 0, (0, 255, 0), -1)

# Display images
cv2.imshow('before', before)
cv2.imshow('after', after)
cv2.imshow('diff', diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
