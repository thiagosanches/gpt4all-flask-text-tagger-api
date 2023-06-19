# gpt4all-flask-text-tagger-api

A small Python and Flask project that utilizes [GPT4All](https://gpt4all.io/index.html) to categorize text using tags. It provides a simple API for tagging text, making it easy to organize and categorize large volumes of text data with accuracy and efficiency.

### Usage

```bash
git clone https://github.com/thiagosanches/gpt4all-flask-text-tagger-api.git
cd gpt4all-flask-text-tagger-api
docker-compose up --detach
```

After the first request, it may take some time for the Docker container to process your request, as it needs to download the large model file which is saved in the `~/.cache` folder within the container. To help with this, there is a volume configured in the docker-compose.yaml file which helps to persist the file. 

It's important to mention that you can checksum the downloaded file to match with the current downloaded version. The model file should be on the `.cache` inside the cloned project. However, I was not able to find the checksums on the official site. So, I'm sharing my results, which worked.

```bash
cd gpt4all-flask-text-tagger-api
sha512sum cache/gpt4all/ggml-gpt4all-j-v1.3-groovy.bin
7b9524294f642084b8e85b1810e7fc5464eebde565950f336bd0f6348295046023a971b75a8842d1ad0979eda58a49fbf6917f35afebd4558b784fe0aba64b8f
```

### Test

**Content**: Pix is an instant payment platform created and managed by the monetary authority of Brazil, the Central Bank of Brazil (BCB),[1] which enables the quick execution of payments and transfers.[2] Pix was announced in the summer of 2019,[3] and was fully operational on November 16, 2020.[1] The \"Pix\" brand name and logo were created in-house by the Central Bank of Brazil in 2020."

```bash
time curl http://localhost:5001/completion -X POST --data '{"content":"Pix is an instant payment platform created and managed by the monetary authority of Brazil, the Central Bank of Brazil (BCB),[1] which enables the quick execution of payments and transfers.[2] Pix was announced in the summer of 2019,[3] and was fully operational on November 16, 2020.[1] The \"Pix\" brand name and logo were created in-house by the Central Bank of Brazil in 2020."}' -H "Content-Type: application/json"
```

### Results

It worked exceptionally well! It successfully extracted three meaningful tags from the aforementioned text: `#PiX #BCB #PaymentsPlatform`, as depicted in the picture below:
![image](https://github.com/thiagosanches/gpt4all-flask-text-tagger-api/assets/5191469/702d63fb-e299-4710-bf8a-67dbdf21b76c)

### Next steps and my personal considerations

Gain a deeper understanding of how it works to fully leverage its potential. This method proves to be the most straightforward way to run a large language model (LLM) on standard consumer hardware. I've explored other approaches previously, but they presented challenges due to the limitations of my hardware.
