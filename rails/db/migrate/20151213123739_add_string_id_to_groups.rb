class AddStringIdToGroups < ActiveRecord::Migration
  def change
    add_column :groups, :string_id, :string
  end
end
