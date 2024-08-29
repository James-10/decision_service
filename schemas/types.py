from ariadne import gql

type_defs = gql("""
    type HousePrediction {
        price: Float!
    }

    input HouseFeaturesInput {
        bedrooms: Int!
        bathrooms: Int!
        sqft_living: Int!
        sqft_lot: Int!
        floors: Int!
    }

    type LGDPrediction {
        lgd: Float!
    }

    input FinancialFeaturesInput {
        loan_amount: Float!
        collateral_value: Float!
        credit_score: Int!
    }

    type Query {
        predictHousePrice(features: HouseFeaturesInput!): HousePrediction!
        predictLGD(features: FinancialFeaturesInput!): LGDPrediction!
    }
""")