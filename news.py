from pprint import pprint
import numpy as np

def request_news():

    titles = ['Appel Announces Breakthrough in Battery Technology',
              'Appel Launches New iPhone Model with 5G Capability',
              'Appel Expands into Healthcare Technology',
              'Global Economic Recovery Boosts Tech Sector',
              'Appel Partners with Leading Car Manufacturer for Autonomous Vehicle Project',
              'Appel Reports Record Sales and Profits for Latest Quarter',
              'Appel Acquires Innovative Augmented Reality Startup',
              'Appel Introduces Sustainable Practices in Supply Chain Management',
              "Positive Reception for Appel's Entry into Wearable Technology Market",
              'Appel Receives Regulatory Approval for New Product Launch',
              'Global Chip Shortage Impacts Apple Production',
              'Apple Faces Antitrust Scrutiny',
              'Cybersecurity Breach Affects Apple Services',
              'Apple Issues Product Recall Due to Safety Concerns'
              ]
    descriptions = ['Significant advancement in battery technology positively impacts product offerings and consumer demand, with effects lasting for a moderate period as competitors catch up.',
 'Launching a highly anticipated iPhone model with advanced capabilities typically leads to increased sales and investor enthusiasm, with effects persisting until the next major product release.',
 'Diversifying into healthcare technology presents new revenue opportunities, though the impact may take time to materialize fully and could last until significant advancements are made in the healthcare sector.',
 'A strong global economic recovery generally benefits technology companies like Appel, though the impact may be moderate and could last until the next economic downturn.',
 'Collaboration on autonomous vehicles represents a potentially lucrative new market for Appel, with effects lasting until significant progress or setbacks occur in the autonomous vehicle industry.',
 'Strong financial performance signals company health and growth potential, typically resulting in a positive reaction from investors, with effects persisting until the next earnings report.',
 "Strategic acquisitions, especially in emerging technologies like augmented reality, can boost investor confidence in Appel's long-term vision, with effects lasting until significant developments or changes in strategy occur.",
 "Implementing sustainable practices may improve Appel's reputation and appeal to environmentally conscious consumers, positively impacting stock sentiment, with effects lasting until significant changes are made in the supply chain.",
 "Successful entry into the wearable technology market could diversify Appel's revenue streams and strengthen its competitive position, with effects lasting until significant advancements or disruptions occur in the wearable technology market.",
 'Regulatory approval for new products clears a significant hurdle and allows Appel to proceed with its plans, potentially driving stock price upward, with effects lasting until significant regulatory changes or challenges occur.',
 "A global chip shortage could significantly disrupt Apple's production and lead to product delays and revenue losses, with effects lasting until chip supply constraints ease or alternative solutions are implemented.",
 "Antitrust investigations pose a significant risk to Apple's business model and could result in regulatory action or legal repercussions, with effects lasting until regulatory decisions are made or significant changes occur in Apple's business practices.",
 'A cybersecurity breach undermines consumer trust and could lead to financial losses and reputational damage for Apple, with effects lasting until trust is restored or significant improvements are made in cybersecurity measures.',
 "Product recalls can lead to financial losses, damage Apple's reputation, and erode consumer confidence in its products, with effects lasting until product safety concerns are addressed or significant changes are made in product development and testing processes."]


    indexes = [6, 7, 5, 4, 6, 7, 5, 4, 5, 5, -7, -6, -5, -6]
    durations = [8, 9, 7, 6, 8, 9, 7, 6, 7, 7, 9, 8, 7, 8]

    transformed_indexes = [i / 10 for i in indexes]
    transformed_indexes = [i ** 3 for i in transformed_indexes]
    transformed_indexes = [i for i in transformed_indexes]

    transformed_durations = [i / 10 for i in durations]
    transformed_durations = [i ** 5 for i in transformed_durations]
    transformed_durations = [i * 5 for i in transformed_durations]

    random_index = np.random.randint(0, len(transformed_indexes) - 1)

    return transformed_indexes[random_index], transformed_durations[random_index], titles[random_index], descriptions[random_index]
