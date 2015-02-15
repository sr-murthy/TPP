# GAP function for printing the JSON object information of a group in the GAP Small Groups # Library.

AsJSONObject := function( G )

  return Concatenation(
    "{\"GAP_ID\": ", String( IdSmallGroup( G ) ), ",",
     "\"GAP_desc\": \"", String( StructureDescription( G ) ), "\",",
     "\"GAP_pickled_ID\": ", "null", ",",
     "\"is_abelian\": ", String( IsAbelian( G ) ), ",",
     "\"comm_length\": ", String( CommutatorLength( G ) ), ",",
     "\"is_cyclic\": ", String( IsCyclic( G ) ), ",",
     "\"is_elem_abelian\": ", String( IsElementaryAbelian( G ) ), ",",
     "\"is_simple\": ", String( IsSimple( G ) ), ",",
     "\"comp_length\": ", String( Size( CompositionSeries( G ) ) - 1 ), ",",
     "\"is_nilpotent\": ", String( IsNilpotent( G ) ), ",",
     "\"nilpotency_class\": ", String( NilpotencyClass( G ) ), ",",
     "\"is_solvable\": ", String( IsSolvable( G ) ), ",",
     "\"derived_length\": ", String( SolvableLength( G ) ), ",",
     "\"is_pgroup\": ", String( IsPGroup( G ) ), ",",
     "\"generators\": \"", String( Generators( G ) ), "\",",
     "\"char_degrees\": \"", String( MyCharacterDegrees( G ) ), "\"}" );

  end;

WriteSmallGroupsJSONFile := function( file_dir, file_name, orders )

  local file, n, num_small_groups, total_groups, total_bytes;

  LoadPackage( "IO" );
  file := IO_File( Concatenation( file_dir, file_name ), "w" );
  total_groups := 0;
  total_bytes := 0;

  IO_WriteLine( file, "[" );
  for n in orders do
    num_small_groups := NumberSmallGroups( n );
    for i in [1..num_small_groups] do
      if total_groups > 0 then
        total_bytes := total_bytes + IO_WriteLine( file, "," );
      fi;
      total_bytes := total_bytes + IO_Write( file, AsJSONObject( SmallGroup( n, i ) ) );
      total_groups := total_groups + 1;
    od;
  od;
  total_bytes := total_bytes + IO_WriteFlush( file, "\n]" );

  IO_Close( file );

  Print( total_groups, " small groups successfully written as JSON objects to file ",
         Concatenation( file_dir, file_name ), " using ", Float( total_bytes / 1024 ),
         " Kb." );

  end;
