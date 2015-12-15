class CreateSteps < ActiveRecord::Migration
  def change
    create_table :steps do |t|
      t.text :message
      t.text :error_message
      t.text :options
      t.integer :step_type
      t.belongs_to :group, index: true, foreign_key: true

      t.timestamps null: false
    end
  end
end
