# from transformers import pipeline
# from transformers.pipelines import TextGenerationPipeline

# # @st.cache(allow_output_mutation=True, suppress_st_warning=True)
# def load_model() -> TextGenerationPipeline:
#     return pipeline("text-generation", model="gpt2")

# text_generator = load_model()

# print(text_generator("I hope this email finds you well! I am a retained recruiter with SealthHealth. Our client is uniquely positioned to improve hundreds of millions of patient outcomes and transform healthcare by vastly improving value-based care in the US. We are recruiting a Head of Product", max_length=1000, do_sample=True))  

# #generated 1
# # [{'generated_text': "I hope this email finds you well! I am a retained recruiter with SealthHealth. Our client is uniquely positioned to improve hundreds of millions of patient outcomes and transform healthcare by vastly improving value-based care in the US. We are recruiting a Head of Product, who can deliver your product across the entire spectrum. The primary focus is to provide personalized medical care through effective patient access, through consistent quality and cost-effectiveness.\n\nMy experience, with this company has been very valuable and I was glad to hear that the opportunity for a recruit to earn your interest came from an important place. Thank you for your interest in a position leading one of the country's biggest hospitals. I now offer you an opportunity to enter the workforce of SealthHealth with an emphasis on delivering better care for your patients. Congratulations, Steve!\n\nPlease read and follow the above links for further information on the relevant opportunities that might be offered, along with appropriate qualifications."}]

# #generated 2
# # [{'generated_text': 'I hope this email finds you well! I am a retained recruiter with SealthHealth. Our client is uniquely positioned to improve hundreds of millions of patient outcomes and transform healthcare by vastly improving value-based care in the US. We are recruiting a Head of Product Engineering with more than two decades of experience on a variety of technology companies that focus on healthcare. If you would like, you can follow these other great posts:\n\nhttps://www.facebook.com/sealthhealth'}]