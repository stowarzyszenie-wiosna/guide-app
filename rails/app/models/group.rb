class Group < ActiveRecord::Base
  belongs_to :scenario
  has_many :steps
end
